# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, nums: List[int], difference: int) -> int:

        dp = defaultdict(int)

        for num in nums:
            dp[num] = dp[num - difference] + 1
            
        return max(dp.values())
