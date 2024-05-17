# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[float('inf') for _ in range(len(matrix))] for j in range(len(matrix[0]))]
        for i in range(len(matrix) - 1, len(matrix)):
            for j in range(len(matrix[0])):
                dp[i][j] = matrix[i][j]
        n , m = len(matrix) , len(matrix[0])
        # print(dp)
        def inbound(row , col):
            if 0 <= row < n and 0 <= col < m:
                return dp[row][col]
            return float('inf')

        for i in range(len(matrix) - 2 , -1 , -1):
            for j in range(len(matrix[0])):
                x = matrix[i][j] + inbound(i + 1 , j)
                y = matrix[i][j] + inbound(i + 1 , j - 1)
                z = matrix[i][j] + inbound(i + 1 , j + 1)
                # print(x,y,z)
                dp[i][j] = min(x , y , z)
        res = float('inf')
        for k in range(len(dp[0])):
            res = min(res , dp[0][k])
        return res


