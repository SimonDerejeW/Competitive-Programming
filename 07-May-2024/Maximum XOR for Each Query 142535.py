# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        arrXor = 0
        k = (1 << maximumBit) - 1
        for num in nums:
            arrXor ^= num
        
        res = []

        for i in range(len(nums) - 1 , -1 , -1):
            x = arrXor ^ k
            res.append(x)
            arrXor ^= nums[i]
        return res
        

