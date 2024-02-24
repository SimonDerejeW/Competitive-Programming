class Solution:
    def countGoodNumbers(self, n: int) -> int:
        space = n // 2
        remainder = n % 2
        
        def pow(x, n):
            if n == 1:
                return x
            elif n == 0:
                return 1
            
            res = pow(x , n//2)
            return (res * res) % (10**9 + 7) if n % 2 == 0 else (res * res * x) % (10**9 + 7)
        
        good = pow(5,(space + remainder)) * pow(4,space)
        return good % (pow(10,9) + 7)
