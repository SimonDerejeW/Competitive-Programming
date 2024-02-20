class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # count = 0
        # oddcount = 0
        # n = len(nums)
        # l = 0

        # for r in range(n):
        #     if nums[r] % 2 != 0:
        #         oddcount += 1

                
        #     while oddcount > k:
        #         if nums[l] % 2 != 0:
        #             oddcount -= 1
        #         l += 1
            
        #     if oddcount == k:
        #         count += 1
        # return count
        

        summ = sum(nums)
        pref = 0
        prefix = []
        
        res = []

        nums.reverse()

        for i in nums:
            pref += i
            prefix.append(pref)
        
        for i in range(len(nums)):
            if i == len(nums) - 1:
                res.append(abs((nums[i] * i) - prefix[i-1]))
            elif i == 0:
                val = (nums[i] * (len(nums) - i - 1)) - (summ - prefix[i])
                res.append(val)
            else:
                val = (nums[i] * (len(nums) - i - 1)) - (summ - prefix[i]) + abs((nums[i] * i) - prefix[i-1]) 
                res.append(val)
        res.reverse()
        return res















