class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = summ = nums[0]

        for i in range(1 , len(nums)):
            summ += nums[i]
            res = max(res , math.ceil(summ / (i + 1)))
        
        return res