# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(row , col):
            count = 0
            if not inbound(row,col) or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            count += 1
            
            
            for v , h in directions:
                new_row = row + h
                new_col = col + v
                count += dfs(new_row , new_col)
            return count


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = max(area , dfs(i,j))
        return area