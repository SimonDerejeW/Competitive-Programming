# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left==0 or right==0:
            return 0
        if left == right:
            return left
        if left == right - 1:
            return left & right
        num1 = left.bit_length()
        num2 = right.bit_length()
        if num1 == num2:
            ans = ['0']*num1
            binary = bin(left)[2:]
            binary1 = bin(right)[2:]
            for i in range(len(binary)):
                if binary[i] != binary1[i]:
                    break
                elif binary[i]=='1' and binary1[i]=='1':
                    ans[i]='1'
            
        
            return int(''.join(ans),2)
        else:
            return 0