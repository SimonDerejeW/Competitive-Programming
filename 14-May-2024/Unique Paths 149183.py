# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def inbound(row , col):
            return (0 <= row < m) and (0 <= col < n)
        @cache
        def dp(row , col):
            if row == m - 1 and col == n - 1:
                return 1
            if not inbound(row , col):
                return 0
            
            new_row = row + 1
            new_col = col + 1

            return dp(row , new_col) + dp(new_row , col)
        return dp(0,0)