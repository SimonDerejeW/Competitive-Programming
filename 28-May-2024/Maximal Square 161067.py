# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n , m = len(matrix), len(matrix[0])
        def inbound(row , col):
            if 0 <= row <= n - 1 and 0 <= col <= m - 1:
                return matrix[row][col]
            return 0
        maxx = 0
        for i in range(n - 1 , -1 , -1):
            for j in range(m - 1, -1, -1):
                if int(matrix[i][j]) == 0:
                    matrix[i][j] = int(matrix[i][j])
                    continue
                x = min(inbound(i + 1 , j), inbound(i, j + 1), inbound(i + 1, j + 1))
                matrix[i][j] = int(matrix[i][j]) + x
                maxx = max(maxx, matrix[i][j])
                
        return maxx * maxx