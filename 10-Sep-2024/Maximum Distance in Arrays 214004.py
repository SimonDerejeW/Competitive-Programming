# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minn = arrays[0][0]
        maxx = arrays[0][-1]
        maxDist =0
        for i in range(1, len(arrays)):
            maxDist = max(maxDist , abs(minn - arrays[i][-1]))
            maxDist = max(maxDist , abs(maxx - arrays[i][0]))
            minn = min(minn, arrays[i][0])
            maxx = max(maxx, arrays[i][-1])
        return maxDist

            