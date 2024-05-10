# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def fib(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            return fib(n-1) + fib(n-2)
        return fib(n)
        