class Solution:
    # def 
    def myPow(self, x: float, n: int) -> float:
        # res = 
        if n == 1:
            return x
        elif n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x , abs(n))
        else: 
            res = self.myPow(x, n//2)

        return res * res * x if n % 2 != 0 else res * res
        
        
