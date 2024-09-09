# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        seen = defaultdict(int)
        result = [[],[]]
        for winner, loser in matches:
            seen[winner] += 0
            seen[loser] -= 1
        for key in seen:
            if seen[key] == 0:
                result[0].append(key)
            elif seen[key] == -1:
                result[1].append(key)
        result[0].sort()
        result[1].sort()
        return result