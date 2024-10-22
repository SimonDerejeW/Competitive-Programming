# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## fast and slow pointers
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(slow,fast)
            if slow == fast:
                break

        fast = nums[0]
        while True:
            if slow == fast:
                return slow
            slow = nums[slow]
            fast = nums[fast]
