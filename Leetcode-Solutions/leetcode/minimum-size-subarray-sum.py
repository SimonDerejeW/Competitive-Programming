class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSub = float("inf")
        l = 0
        summ = 0
        for r in range(len(nums)):
            summ+=nums[r]
            while summ >= target:
                minSub = min(minSub, r-l+1)
                summ-=nums[l]
                l+=1
        # print(summ)
        if minSub == float("inf"):
            return 0
        return minSub


            
            