# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(idx , bought):
            if idx >= len(prices):
                return 0
            if bought:
                sell = dp(idx + 1 , False) + prices[idx] - fee
                hold = dp(idx + 1 , True)
                return max(sell , hold)
            else:
                buy = dp(idx + 1 , True) - prices[idx]
                hold = dp(idx + 1 , False)
                return max(buy , hold)
        return dp(0 , False)