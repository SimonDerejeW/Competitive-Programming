class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score = 0
        res = 0
        left = 0
        count = {}

        for right in range(len(nums)):
            res += nums[right]
            count[nums[right]] = 1 + count.get(nums[right], 0)
            
            while count[nums[right]] > 1:
                res -= nums[left]
                count[nums[left]]-=1
                if count[nums[left]] == 0:
                    count.pop(nums[left])
                left += 1

            score = max(score,res)
            
        return score
            