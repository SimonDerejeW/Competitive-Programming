# Problem: Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(idx,bought):
            if idx >= len(prices):
                return 0
            
            if bought:
                sell = dp(idx + 1, False) + prices[idx]
                hold = dp(idx + 1, True)
                return max(sell,hold)
            else:
                bought = dp(idx + 1, True) - prices[idx]
                hold = dp(idx + 1, False)
                return max(bought, hold)
        return dp(0,False)