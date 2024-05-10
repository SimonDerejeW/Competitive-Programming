# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        # memo = defaultdict(int)
        # def helper(n):
        #     if n == 0:
        #         return 0
        #     elif n == 1:
        #         return 1
        #     elif n == 2:
        #         return 1
            
        #     summ = 0
        #     if memo[n - 1]:
        #         summ+= memo[n - 1]
        #     else:
        #         x = helper(n - 1)
        #         memo[n-1] = x
        #         summ += x
        #     if memo[n - 2]:
        #         summ+= memo[n - 2]
        #     else:
        #         y = helper(n - 2)
        #         memo[n-2] = y
        #         summ += y
        #     if memo[n - 3]:
        #         summ+= memo[n - 3]
        #     else:
        #         z = helper(n - 3)
        #         memo[n-3] = z
        #         summ += z
        #     return summ

        # return helper(n)
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1

        if n > 1:
            for i in range(3 , n+1):
                memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        return memo[n]