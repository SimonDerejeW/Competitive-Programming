# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        left = 0
        for right in range(len(prices)):
            if prices[left] <= prices[right]:
                profit = max(profit , (prices[right] - prices[left]))
            else:
                left = right
        return profit

        