from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        res = []
        size = len(p)
        count = Counter(p)
        if count == Counter(s[:len(p)]):
            res.append(0)
        l = 1
        for i in range(size,len(s)):
            if count == Counter(s[l:i+1]):
                res.append(l)
            l+=1
        return res

