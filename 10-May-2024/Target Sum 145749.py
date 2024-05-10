# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dp(idx , summ):
            if idx >= n and summ == target:
                return 1
            if idx >= n:
                return 0
            
            return dp(idx + 1, summ + nums[idx]) + dp(idx + 1 , summ - nums[idx])

        return dp(0 , 0)
        # return count