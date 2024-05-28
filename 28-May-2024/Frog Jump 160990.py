# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        @cache
        def dp(idx, steps):
            if idx + 1 >= n:
                return True
            
            ans = False
            for i in range(idx + 1, n):
                difference = stones[i] - stones[idx]
                if steps - 1 <= difference <= steps + 1:
                    ans = ans or dp(i,difference)
                
            return ans
        return dp(0,0)