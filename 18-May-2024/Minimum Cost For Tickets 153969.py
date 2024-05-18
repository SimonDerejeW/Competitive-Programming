# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(idx, day):
            if idx >= len(days):
                return 0

            if days[idx] > day:
                return min(
                    dp(idx+1, days[idx]) + costs[0], 
                    dp(idx+1, days[idx] + 6 ) + costs[1], 
                    dp(idx+1, days[idx] + 29 ) + costs[2]
                    )
            else:
                return dp(idx+1, day)
        return dp(0, 0)