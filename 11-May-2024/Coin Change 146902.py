# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(total):
            if total == amount:
                return 0
            if total > amount:
                return float('inf')
            res = float('inf')
            for num in coins:
                res = min(res , 1 + dp(total + num))
            return res

        answer = dp(0)
        if answer == float('inf'):
            return -1
        return answer
            
                

                