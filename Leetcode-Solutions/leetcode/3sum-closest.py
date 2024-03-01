class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # res = set()
        summ = float("inf")
        ans = 0
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                x = nums[i] + nums[l] + nums[r]
                if summ > abs(x - target):
                    summ = abs(x - target)
                    ans = x
                if nums[i] + nums[l] + nums[r] > target:
                    if summ > abs(x - target):
                        summ = abs(x - target)
                        ans = x
                    r -=1
                elif nums[i] + nums[l] + nums[r] < target:
                    l+=1
                else:
                    ans = nums[i] + nums[l] + nums[r]
                    break
        return ans