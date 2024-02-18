class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = {0: 1}
        maxSub = 0
        summ = 0

        for i in range(len(nums)):
            summ += nums[i]
            diff = summ - goal

            maxSub += prefix.get(diff,0)
            prefix[summ] = 1 + prefix.get(summ,0)
        
        return maxSub
