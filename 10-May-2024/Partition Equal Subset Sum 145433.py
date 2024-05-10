# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        target = total_sum / 2
        if total_sum % 2:
            return False

        @cache
        def dp(idx , summ):
            if idx >= n or summ == target:
                return summ == target
            
            return dp(idx + 1 , summ + nums[idx]) or dp(idx + 1 , summ)
        return dp(0 , 0)