class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        target = nums[-1]
        op = 0
        for i in range(len(nums)-2, -1 ,-1):
            if nums[i] > target:
                op += math.ceil(nums[i] / target) - 1
                # previously  target = nums[i] // target
                target = nums[i] // math.ceil(nums[i] / target)
            
            # updates if the next number is less than the current target
            elif nums[i] < target:
                target = nums[i]
        
        return op
