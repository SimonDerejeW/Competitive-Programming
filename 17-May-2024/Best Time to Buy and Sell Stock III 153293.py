# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dp(idx , bought):
            if idx >= n:
                return 0
            if bought > 3:
                return 0
            
            if bought % 2:
                sell = dp(idx + 1 , bought + 1) + prices[idx]
                hold = dp(idx + 1 , bought)
                return max(sell , hold)
            else:
                buy = dp(idx + 1 , bought + 1) - prices[idx]
                hold = dp(idx + 1 , bought)
                return max(buy , hold)
        return dp(0,0)