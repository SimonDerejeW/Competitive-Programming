# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        k = 1
        dxn = 1
        while time != 0:
            k += dxn
            if k == 1 or k == n:
                dxn *= -1
            time -= 1
        return k

