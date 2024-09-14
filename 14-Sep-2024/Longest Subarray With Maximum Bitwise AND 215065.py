# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        maxLen = 0
        total = 0
        for i in range(len(nums)):
            if nums[i] == max_num:
                total += 1
            else:
                total = 0
            maxLen = max(total, maxLen)
        return maxLen

        

