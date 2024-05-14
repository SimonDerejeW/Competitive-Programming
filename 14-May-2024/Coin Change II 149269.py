# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        n = len(coins)
        @cache
        def dp(idx , total):
            if idx >= n:
                return 0
            if total == amount:
                return 1
            if total > amount:
                return 0

            x = dp(idx + 1 , total)
            y = dp(idx, total + coins[idx])
            ans = x+y
            
            return ans
        return dp(0,0)
