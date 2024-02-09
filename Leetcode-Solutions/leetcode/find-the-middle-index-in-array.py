class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pref = []
        suff = []

        prefSum = suffSum = 0

        for i in nums:
            prefSum += i
            pref.append(prefSum)
        
        for i in nums[::-1]:
            suffSum += i
            suff.append(suffSum)
        
        suff.reverse()

        for i in range(len(nums)):
            if pref[i] == suff[i]:
                return i
        return -1
        

        