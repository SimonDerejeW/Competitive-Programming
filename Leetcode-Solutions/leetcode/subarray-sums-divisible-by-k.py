class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = {0:1}
        maxSub = 0
        summ = 0

        for i in nums:
            summ += i
            remainder = summ%k
            maxSub += pref.get(remainder, 0)
            pref[remainder] = 1 + pref.get(remainder,0)
        
        return maxSub
