# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(i, j, turn):
            if i >= j:
                return 0

            if turn:
                x = dp(i + 1, j, False) + piles[i]
                y = dp(i, j - 1, False) + piles[j]
                return max(x , y)
            else:
                x = dp(i + 1, j, True)- piles[i]
                y = dp(i, j - 1, True)- piles[i]
                return min(x , y)

        return dp(0, len(piles) - 1, True)
