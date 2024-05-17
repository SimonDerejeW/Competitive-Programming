# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        dp = [[0 for i in range(m)] for j in range(n)]
        if grid[-1][-1]:
            return 0
        dp[-1][-1] = 1
        # print(dp)

        def inbound(row , col):
            if 0 <= row < n and 0 <= col < m and grid[row][col] != 1:
                return dp[row][col]
            return 0
        
        for i in range(n - 1 , -1 , -1):
            for j in range(m - 1 , -1 , -1):
                if grid[i][j] == 0:
                    down = inbound(i + 1, j)
                    right = inbound(i , j + 1)
                    dp[i][j] += down + right
        # print(dp)
        return dp[0][0]