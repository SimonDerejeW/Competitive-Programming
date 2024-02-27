class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        seen = []
        align = 0
        mx = 0
        for i in range(len(flips)):
            mx = max(mx , flips[i])
            if mx == i + 1:
                align += 1

        return align