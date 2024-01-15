from typing import List
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)
        played_matches = set()

        for winner, loser in matches:
            losses[loser] += 1
            played_matches.add(winner)
            played_matches.add(loser)

        winners = [player for player in played_matches if losses[player] == 0]
        one_loss_players = [player for player in played_matches if losses[player] == 1]

        winners.sort()
        one_loss_players.sort()

        return [winners, one_loss_players]
