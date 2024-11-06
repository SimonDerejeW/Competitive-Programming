# Problem: Arithmetic Subarrays - https://leetcode.com/problems/arithmetic-subarrays/

class Solution:

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res=[]
        
        for i in range(len(l)):
            sub=nums[l[i]:r[i]+1]
            sub.sort()
            count=False
            d=sub[1]-sub[0]
            for j in range(1,len(sub)):
                if sub[j]-d==sub[j-1]:
                    count=True
                else:
                    count=False
                    break
            res.append(count)
        return res