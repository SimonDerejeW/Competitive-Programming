class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sliding_window = sum(nums[:k])
        max_avg = sliding_window/k
        for i in range(k,len(nums)):
            sliding_window += nums[i] - nums[i-k]
            x = sliding_window/k
            if x > max_avg:
                max_avg = x
        return max_avg

        # max = sum(nums[:k])/k
        # i = 0
        # size = len(nums)
        # while i <= size - k:
        #     avg = sum(nums[i:i+k])/k 
        #     if avg > max:
        #         max = avg
        #     i+=1
        # return max