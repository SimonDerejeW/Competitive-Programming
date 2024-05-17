# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        
        dp = [[False for i in range(m+1)] for j in range(n + 1)]
        for k in range(m+1):
            dp[0][k] = True
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]

