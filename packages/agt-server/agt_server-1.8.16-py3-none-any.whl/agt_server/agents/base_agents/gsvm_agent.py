import json
import random
import numpy as np
import pkg_resources
import threading
from agt_server.agents.base_agents.agent import Agent
from agt_server.agents.base_agents.game_report import GameReport
from agt_server.utils import extract_first_json

class GSVM9Agent(Agent):
    """
    A minimal example agent for a GSVM-9 style server-based auction.
    Tracks whether it's a National or Regional bidder, capacity, valuations, etc.
    """

    def __init__(self, name=None, timestamp=None):
        super().__init__(name, timestamp)
        # Load config if you want (e.g., response time)
        config_path = pkg_resources.resource_filename('agt_server', 'configs/server_configs/sa_config.json')
        with open(config_path) as cfile:
            self.config = json.load(cfile)
        self.response_time = self.config.get('response_time', 2)

        # Auction-related fields
        self.num_goods = None
        self.goods = None
        self.valuations = {}
        self._goods_to_index = {}
        self._index_to_goods = {}

        # Role & capacity
        self.is_national_bidder = False
        self.is_regional_bidder = False
        self.capacity = 3  # default, overwritten if national

        # Timeout tracking
        self.timeout = False
        self.global_timeout_count = 0
        self.round_number = 0

    def timeout_handler(self):
        print(f"{self.name} has timed out")
        self.timeout = True

    def handle_permissions(self, resp):
        """
        If the server sends post-round data about what we did, payments, etc.
        you can store it in game_report.
        """
        self.player_type = resp.get('player_type')
        gh = self.game_report.game_history

        # Example usage: store the last round’s data
        gh.setdefault('my_bid_history', []).append(resp.get('my_bid'))
        gh.setdefault('my_utils_history', []).append(resp.get('my_util'))
        gh.setdefault('my_payment_history', []).append(resp.get('payments'))
        gh.setdefault('price_history', []).append(resp.get('prices'))
        gh.setdefault('winner_history', []).append(resp.get('winners'))

    def handle_postround_data(self, resp):
        self.global_timeout_count = resp.get('global_timeout_count', 0)
        self.handle_permissions(resp)

    def get_bids(self):
        """
        Produce a dictionary: {good_name: bid_value, ...}.
        Here we do a naive approach: we bid our entire valuation on each good
        we are eligible for. If we want to ensure we don't exceed capacity
        (for example, 6 for national, 3 for regional), we could do something more
        sophisticated, but typically the server enforces capacity anyway.
        """
        bid_dict = {}
        # Example: bid entire valuation on each good with valuation > 0
        for good, val in self.valuations.items():
            if val > 0:
                bid_dict[good] = val
            else:
                bid_dict[good] = 0
        return bid_dict

    def get_action(self):
        """
        Called by the server to get your bid dictionary each round.
        """
        return self.get_bids()

    def print_results(self):
        """
        Prints a summary of the current game results based on the game history.
        """
        gh = self.game_report.game_history

        last_bid = gh.get('my_bid_history', [])[-1] if gh.get('my_bid_history') else None
        last_winners = gh.get('winner_history', [])[-1] if gh.get('winner_history') else None
        last_prices = gh.get('price_history', [])[-1] if gh.get('price_history') else None
        last_payment = gh.get('my_payment_history', [])[-1] if gh.get('my_payment_history') else None
        last_util = gh.get('my_utils_history', [])[-1] if gh.get('my_utils_history') else None

        self.round_number += 1
        print(f"----- Round {self.round_number} Results for {self.name} -----")
        print(f"Bidder Type: {'National' if self.is_national_bidder else 'Regional'}")
        print(f"Last Bid: {last_bid}")
        print(f"Winners: {last_winners}")
        print(f"Prices: {last_prices}")
        print(f"My Payment: {last_payment}")
        print(f"My Utility This Round: {last_util}")
        print("-----------------------------------------\n")

    def play(self):
        """
        Main loop for interacting with the GSVM-9 (or similar) server game.
        Listens for messages and responds appropriately.
        """
        # 1. Possibly read initial handshake
        data = self.client.recv(1024).decode()
        data = extract_first_json(data)
        if data:
            resp = json.loads(data)
            if resp.get('message') == 'provide_game_name':
                print(f"We are playing {resp.get('game_name')}")
                message = {"message": "game_name_recieved"}
                self.client.send(json.dumps(message).encode())
                self.restart()

        # 2. Main loop
        while True:
            data = self.client.recv(10000).decode()
            data = extract_first_json(data)
            if not data:
                continue
            request = json.loads(data)

            msg_type = request.get('message')
            if msg_type == 'send_preround_data':
                # The server tells us whether we are national or regional
                # in addition to valuations, etc.
                self.is_national_bidder = request.get('is_national', False)
                self.is_regional_bidder = not self.is_national_bidder
                # capacity = 6 if national, else 3
                self.capacity = 6 if self.is_national_bidder else 3

                self.num_goods = request.get('num_goods')
                goods_list = request.get('goods', [])
                self.goods = set(goods_list)

                # Build index mappings
                self._goods_to_index = {good: idx for idx, good in enumerate(goods_list)}
                self._index_to_goods = {idx: good for good, idx in self._goods_to_index.items()}

                # Retrieve valuations from the server
                valuations_dict = request.get('valuations', {})
                self.valuations = {}
                for good in goods_list:
                    self.valuations[good] = valuations_dict.get(good, 0.0)

                # Acknowledge
                self.client.send(json.dumps({"message": "preround_data_recieved"}).encode())

            elif msg_type == 'request_bid':
                # The server wants our bid dictionary
                self.timeout = False
                try:
                    timer = threading.Timer(self.response_time, self.timeout_handler)
                    timer.start()
                    bid = self.get_action()
                finally:
                    if self.timeout:
                        bid = None
                    timer.cancel()

                try:
                    self.client.send(json.dumps({
                        "message": "provide_bid",
                        "bid": bid,
                        "timeout": self.timeout
                    }).encode())
                except Exception as e:
                    print(f"Error sending bid: {e}")

            elif msg_type == 'prepare_next_round':
                # The server is telling us the round is over
                self.print_results()
                self.handle_postround_data(request)
                self.update()
                self.client.send(json.dumps({"message": "ready_next_round"}).encode())

            elif msg_type == 'prepare_next_game':
                # The server is telling us the game ended and a new one will begin
                self.print_results()
                self.restart()
                self.client.send(json.dumps({"message": "ready_next_game"}).encode())

            elif msg_type == 'game_end':
                # The entire game is finished
                if request.get('send_results'):
                    try:
                        df = pd.read_json(request['results'])
                        if df is not None:
                            print(df)
                    except:
                        print("Results too large. Please check with your TA.")
                else:
                    print(request.get('results'))
                self.close()
                break

            elif msg_type == 'disqualified':
                # We were disqualified
                dq_msg = request.get('disqualification_message', '')
                if dq_msg:
                    print(dq_msg)
                self.close()
                break
