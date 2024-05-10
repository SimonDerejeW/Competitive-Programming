# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[i] , nums[0])
            return max(dp(i - 1) , dp(i - 2) + nums[i])
        return dp(len(nums) - 1)
        