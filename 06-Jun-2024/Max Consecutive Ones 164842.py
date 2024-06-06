# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        max_cons = 0
        i=0
        l = 0
        r = 0
        while i < len(nums)-1:
            while nums[i] == 1:
                r+=1
                i+=1
            else: 
                if max_cons < (r-l):
                    max_cons = (r-l)
                i+=1
                r+=1
                l=r
        return max_cons
