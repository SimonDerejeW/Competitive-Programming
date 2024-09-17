# Problem: Number of Closed Islands - https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        n = len(grid)
        m = len(grid[0])

        def inbound(row, col):
            return ((0 <= row < n) and (0 <= col < m) and (grid[row][col] == 0))


        def dfs(row, col):
            grid[row][col] = 1
            for x, y in directions:
                new_row = row + x
                new_col = col + y

                if inbound(new_row,new_col):
                    dfs(new_row,new_col)
        
        for i in range(m):
            if grid[0][i] == 0:
                dfs(0,i)
        for j in range(n):
            if grid[j][0] == 0:
                dfs(j,0)
        for k in range(m):
            if grid[n-1][k] == 0:
                dfs(n - 1,k)
        for l in range(n):
            if grid[l][m-1] == 0:
                dfs(l,len(grid[0]) - 1)
        
        count = 0
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == 0:
                    count += 1
                    dfs(a,b)
        return count