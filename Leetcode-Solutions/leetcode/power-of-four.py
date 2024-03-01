class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def recursion(n):
            if n == 1:
                return True
            elif n<1:
                return False
            else:
                n = n/4
                return recursion(n)
        return recursion(n)