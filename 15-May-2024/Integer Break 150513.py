# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 3:
            return 2
        elif n == 2:
            return 1
        @cache
        def dp(num):
            if num == 1:
                return 1
            res = num
            for i in range(1 , num):
                x = num - i
                res = max(res , i * dp(x))
            return res
        return dp(n)
