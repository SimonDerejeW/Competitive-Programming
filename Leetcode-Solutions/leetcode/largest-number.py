class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(x == 0 for x in nums):
            return '0'
        size = len(nums)
        for i in range(size):
            for j in range(size-i-1):
                if str(nums[j]) + str(nums[j+1]) < str(nums[j+1]) + str(nums[j]):
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        def convert(x):
            return str(x)
        return ''.join(list(map(convert, nums)))