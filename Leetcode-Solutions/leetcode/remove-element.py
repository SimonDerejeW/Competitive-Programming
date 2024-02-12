class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        unique_index = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[unique_index] = nums[i]
                unique_index += 1
        return unique_index
