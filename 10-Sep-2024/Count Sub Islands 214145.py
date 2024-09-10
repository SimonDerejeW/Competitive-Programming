# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        flag = True
        sub_islands = 0

        def inbound(row, col):
            return (0 <= row < len(grid2) and 0 <= col < len(grid2[0]) and grid2[row][col] == 1)
        
        def dfs(row, col):
            nonlocal flag
            grid2[row][col] = 0

            for v , h in directions:
                new_row = row + v
                new_col = col + h
                if inbound(new_row, new_col):
                    if grid1[new_row][new_col] != 1:
                        flag = False
                    dfs(new_row, new_col)
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    flag = True
                    dfs(i,j)
                    if flag and grid1[i][j] == 1:
                        sub_islands += 1
        
        return sub_islands

