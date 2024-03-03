class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # stack = []
        # for i in range(len(nums)):
        #     while stack and stack[-1] >= nums[i]:
        #         stack.pop()
        #     stack.append(nums[i])
        #     if len(stack) >= 3:
        #         return True
        # return False
        min1 = float("inf")
        min2 = float("inf")

        for num in nums:
            if num > min2:
                return True
            if num > min1:
                min2 = min(min2, num)
            min1 = min(min1 , num)
        return False
        