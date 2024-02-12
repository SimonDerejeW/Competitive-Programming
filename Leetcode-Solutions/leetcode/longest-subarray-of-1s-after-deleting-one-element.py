class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = {}
        l = 0
        maxSub = 0

        for r in range(len(nums)):
            count[nums[r]] = 1 + count.get(nums[r], 0)
            
            while 0 in count and count[0] > 1:
                count[nums[l]] -=1
                if count[nums[l]] == 0:
                    count.pop(nums[l])
                l+=1
            maxSub = max(maxSub, r-l)
        return maxSub