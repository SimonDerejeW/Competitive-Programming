# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        @cache
        def dp(i, j):
            if i >= n or j >= m:
                return 0

            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)
            else:
                return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)
