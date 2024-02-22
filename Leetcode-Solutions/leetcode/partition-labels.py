class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        size = 0
        right = 0
        res = []

        for i in range(len(s)):
            lastIndex[s[i]] = i
        
        for i in range(len(s)):
            right = max(right, lastIndex[s[i]])
            size += 1
            if i == right:
                res.append(size)
                size = 0
        return res

        
