# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n , m = len(dungeon) , len(dungeon[0])
        dp = [[float('-inf') for i in range(m)] for j in range(n)]
        dp[-1][-1] = dungeon[-1][-1]

        def inbound(row , col):
            if 0 <= row < n and 0 <= col < m:
                return dp[row][col]
            return float('-inf')

        for i in range(n - 1 , -1 , -1):
            for j in range(m - 1 , -1 , -1):
                x = inbound(i + 1 , j)
                y = inbound(i , j + 1)
                maxx = max(x , y)
                if maxx != float('-inf'):
                    dp[i][j] = max(x , y) + dungeon[i][j]
                else:
                    dp[i][j] = dungeon[i][j]

                if dp[i][j] > 0:
                    dp[i][j] = 0
        ans = dp[0][0]
        if ans >= 0:
            return 1
        return abs(ans) + 1
