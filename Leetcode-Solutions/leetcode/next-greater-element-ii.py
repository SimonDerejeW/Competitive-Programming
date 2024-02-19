class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        stack = []
        n = len(nums)
        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                ans[stack[-1]] = nums[idx]
                stack.pop()
            stack.append(idx)
        return ans