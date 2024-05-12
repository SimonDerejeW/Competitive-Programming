# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dp(idx , bought, sold):
            if idx >= n:
                return 0

            if sold:
                x = dp(idx + 1 , False , False)
                return x
            elif bought:
                sell = dp(idx + 1 , False , True) + prices[idx]
                hold = dp(idx + 1 , True, False)
                return max(sell , hold)
            else:
                buy = dp(idx + 1 , True, False) - prices[idx]
                hold = dp(idx + 1 , False, False)
                return max(buy , hold)
        return dp(0 , False, False)