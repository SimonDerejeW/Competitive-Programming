# Problem: Next Permutation - https://leetcode.com/problems/next-permutation/description/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # First find the idx we need to swap: the first idx out of the increasing order from the right
        idx = len(nums) - 2
        minn = float('inf')
        other_idx = -1
        while idx >= 0 and nums[idx] >= nums[idx + 1]:
            idx -= 1

        # Find the smallest number's index to the right of this index
        if idx >= 0:
            other_idx = len(nums) - 1
            while nums[idx] >= nums[other_idx]:
                other_idx -= 1
            nums[idx], nums[other_idx] = nums[other_idx], nums[idx]

        
        nums[idx+1:] = reversed(nums[idx+1:])
        

        