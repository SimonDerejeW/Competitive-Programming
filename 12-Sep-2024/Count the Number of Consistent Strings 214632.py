# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(list(allowed))
        consistent = 0
        for word in words:
            flag = True
            for char in word:
                if char not in allowed:
                    flag = False
            if flag:
                consistent += 1
        return consistent
                