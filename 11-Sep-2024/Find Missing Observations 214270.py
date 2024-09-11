# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = sum(rolls)
        remain = ((m+n)*mean) - total
        
        if (remain < n) or (remain > (6 * n)):
            return []
        
        arr = [1] * n
        remain -= n

        for i in range(n):
            if remain == 0:
                break
            if remain >= 5:
                arr[i] += 5
                remain -= 5
            else:
                arr[i] += remain
                break
        return arr
