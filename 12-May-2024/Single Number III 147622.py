# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        arrXor = 0
        for num in nums:
            arrXor ^= num
        
        i = 0
        while True:
            if arrXor & 1 << i:
                break
            i += 1
        
        mask = 1 << i
        num1 = 0
        for num in nums:
            if num & mask:
                num1 ^= num
        return [num1 , num1 ^ arrXor]