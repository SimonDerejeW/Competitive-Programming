# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        # capital = w
        nums = list(zip(capital , profits))
        nums.sort()

        i , j = 0 , 0
        while i < len(nums):
            while j < len(nums) and nums[j][0] <= w:
                heappush(heap , -nums[j][1])
                j += 1
            if heap:
                w += (-heappop(heap))
                k -= 1
            else:
                break
            if k == 0:
                return w
            i = j
        while k and heap:
            w += (-heappop(heap))
            k -= 1
        return w


            
