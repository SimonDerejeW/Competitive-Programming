class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        summ = 0

        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                total = grid[row][col] + grid[row][col + 1] + grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]
                summ = max(summ , total)
        
        return summ