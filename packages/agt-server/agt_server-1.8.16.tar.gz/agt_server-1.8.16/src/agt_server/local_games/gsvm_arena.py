import random
import numpy as np
import pandas as pd
from collections import defaultdict
from agt_server.local_games.base import LocalArena

class GSVM9Arena(LocalArena):
    """
    A local arena for the GSVM-9 Auction with:
      - 4 Bidders: [National, Regional1, Regional2, Regional3]
      - 9 Goods: A..I
      - Uniform(0, maxVal) valuations from the table
      - Global synergy: (1 + 0.2*(n-1)) * sum_of_valuations
      - Capacity: National can win up to 6 goods, Regionals up to 3 each
    """

    def __init__(self,
                 players=[],
                 num_rounds=10,
                 timeout=1,
                 handin=False,
                 logging_path=None,
                 save_path=None):
        """
        :param players: List of exactly 4 players [N, R1, R2, R3].
        :param num_rounds: Number of rounds in the repeated game.
        :param timeout: Timeout in seconds for get_action calls.
        :param handin: Boolean indicating whether to suppress prints and store logs in a file.
        :param logging_path: File path for logging if handin=True.
        :param save_path: Path for final results if handin=True.
        """
        super().__init__(num_rounds, players, timeout, handin, logging_path, save_path)

        # We expect exactly 4 players: 1 national, 3 regional.
        assert len(self.players) == 4, "GSVM-9 requires exactly 4 players."

        # Define the set of goods
        self.goods = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        self.game_name = "GSVM-9 Auction"

        # Max valuations from the table (blank entries => 0 => not eligible)
        # By default, assume players[0] = National, players[1..3] = Regionals
        self.max_valuations = [
            # National Bidder
            {"A":15, "B":15, "C":30, "D":30, "E":15, "F":15, "G":0,  "H":0,  "I":0},
            # Regional Bidder 1
            {"A":20, "B":20, "C":40, "D":40, "E":20, "F":0,  "G":20, "H":0,  "I":0},
            # Regional Bidder 2
            {"A":0,  "B":40, "C":40, "D":20, "E":20, "F":0,  "G":0,  "H":20, "I":0},
            # Regional Bidder 3
            {"A":20, "B":20, "C":0,  "D":20, "E":20, "F":20, "G":0,  "H":0,  "I":20}
        ]

        # Capacity: National = 6, Regionals = 3
        self.capacity = [6, 3, 3, 3]

        # Initialize game reports
        for idx, player in enumerate(self.players):
            self.game_reports[player.name] = {
                "valuation_history": [],
                "bid_history": [],
                "util_history": [],
                "index": idx,
                "global_timeout_count": 0
            }

        self.results = []
        self.game_num = 1

    def run(self):
        """
        Run the entire repeated auction for self.num_rounds rounds.
        """
        # Restart all agents first
        for player in self.players:
            self.run_func_w_time(player.restart, self.timeout, player.name)

        # Conduct the auction
        self.run_game(self.players)

        # Summarize final results
        results = self.summarize_results()
        return results

    def run_game(self, group):
        """
        Run all rounds of the auction among these 4 players.
        """
        for round_idx in range(self.num_rounds):
            self._log_or_print(f"Round {round_idx+1} of {self.num_rounds} in {self.game_name}")
            # 1) Assign valuations
            for i, player in enumerate(group):
                valuations = {}
                for good in self.goods:
                    max_val = self.max_valuations[i].get(good, 0)
                    if max_val > 0:
                        valuations[good] = random.uniform(0, max_val)
                    else:
                        valuations[good] = 0.0  # ineligible => 0
                # Store the valuations in the agent
                player.valuations = valuations
                # Save in game_reports
                self.game_reports[player.name]["valuation_history"].append(valuations)

            # 2) Gather bids
            bids = {}
            for player in group:
                bid_dict = self.run_func_w_time(player.get_action, self.timeout, player.name, {})
                if not isinstance(bid_dict, dict):
                    bid_dict = {}
                bids[player.name] = bid_dict
                self.game_reports[player.name]["bid_history"].append(bid_dict)

            # 3) Compute outcome (respect capacity)
            allocation, payments = self.compute_auction_result(bids)

            # 4) Compute synergy-based utility
            for i, player in enumerate(group):
                # Identify which goods were won
                won_goods = [g for g, w in allocation.items() if w == player.name]
                # Sum of valuations for these goods
                base_sum = sum(player.valuations.get(g, 0) for g in won_goods)
                n = len(won_goods)
                synergy_val = (1 + 0.2*(n-1)) * base_sum if n > 0 else 0
                cost = payments[player.name]
                util = synergy_val - cost

                self.game_reports[player.name]["util_history"].append(util)
                # Optionally store in the player's game_report object:
                if hasattr(player, 'game_report'):
                    if "my_utils_history" not in player.game_report.game_history:
                        player.game_report.game_history["my_utils_history"] = []
                    player.game_report.game_history["my_utils_history"].append(util)

            # 5) Let agents update
            for player in group:
                self.run_func_w_time(player.update, self.timeout, player.name)

            self.game_num += 1

        # After finishing all rounds, print each player's total utility
        for player in group:
            tot = sum(self.game_reports[player.name]["util_history"])
            self._log_or_print(f"{player.name} final total utility: {tot}")

    def compute_auction_result(self, bids):
        """
        For each good, assign it to the highest bidder that hasn't exceeded capacity
        and is eligible to bid on that good (i.e., might have a positive max_valuation).
        Returns (allocation, payments) just like in SAArena.
        """
        allocation = {}
        payments = {p.name: 0 for p in self.players}
        # Track how many goods each player has won so far in this round
        capacity_used = defaultdict(int)

        for good in self.goods:
            best_bid = None
            best_player = None
            best_player_idx = None
            for i, player in enumerate(self.players):
                # skip if capacity used is already at max
                if capacity_used[player.name] >= self.capacity[i]:
                    continue
                # skip if ineligible (max_valuation is 0 => can't place positive bid)
                if self.max_valuations[i].get(good, 0) <= 0:
                    continue

                # actual bid
                val = bids[player.name].get(good, 0) or 0
                if (best_bid is None) or (val > best_bid):
                    best_bid = val
                    best_player = player.name
                    best_player_idx = i

            allocation[good] = best_player
            if best_player is not None and best_bid is not None and best_bid > 0:
                payments[best_player] += best_bid
                capacity_used[best_player] += 1

        return allocation, payments

    def summarize_results(self):
        """
        Summarize results across all rounds:
        - total utility
        - average utility per round
        """
        summary_data = []
        for player in self.players:
            name = player.name
            util_list = self.game_reports[name]["util_history"]
            total_util = sum(util_list)
            avg_util = total_util / len(util_list) if util_list else 0
            summary_data.append([name, total_util, avg_util])

        df = pd.DataFrame(summary_data, columns=["Player", "Total Utility", "Avg Utility"])
        df = df.sort_values("Total Utility", ascending=False)
        self._log_or_print(f"\nFinal GSVM-9 Auction Results:\n{df}\n")
        return df
