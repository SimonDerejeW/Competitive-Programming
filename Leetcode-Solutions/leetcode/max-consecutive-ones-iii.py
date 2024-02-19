class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        seen = {0: 0, 1: 0}
        left = 0
        maxCount = 0

        for right in range(len(nums)):
            seen[nums[right]] += 1
            while seen[0] > k:
                seen[nums[left]] -= 1
                left += 1
            maxCount = max(maxCount, right - left + 1)
        
        return maxCount