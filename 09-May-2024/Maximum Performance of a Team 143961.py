# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        nums = list(zip(efficiency , speed))
        nums.sort(reverse=True)
        mod = 10 ** 9 + 7
        heap = []

        j = 0
        summ = 0
        maxPer = 0
        
        for i in range(len(nums)):
            heappush(heap , nums[i][1])
            summ += nums[i][1]
            if len(heap) > k:
                x = heappop(heap)
                summ -= x
            maxPer = max(maxPer , summ * nums[i][0])
        return maxPer % mod



