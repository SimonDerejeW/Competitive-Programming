class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pref = [0] * len(nums)
        res = 0
        for i , j in requests:
            pref[i] += 1
            if j + 1 < len(nums):
                pref[j + 1] -= 1
        
        pref = list(accumulate(pref))
        pref.sort(reverse = True)
        nums.sort(reverse = True)

        for i in range(len(nums)):
            res += (nums[i] * pref[i])
        
        return res % (10 ** 9 + 7)


        

        