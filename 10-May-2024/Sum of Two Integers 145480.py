# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask != 0:
            temp = a
            a = a ^ b
            b = temp & b
            b *= 2

        return (mask&a) if b > 0 else a