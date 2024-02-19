class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxSum = float("-inf")
        # for i in range(len(nums)):
        #     curSum = 0
        #     for j in range(i,len(nums)):
        #         curSum += nums[j]
        #         maxSum = max(maxSum, curSum)
        
        # return maxSum
        maxSum = nums[0]
        curSum = 0

        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSum = max(maxSum, curSum)
        
        return maxSum