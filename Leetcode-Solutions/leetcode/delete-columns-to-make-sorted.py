class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = []
        for i in range(len(strs)-1):
            for j in range(len(strs[0])):
                if strs[i][j] > strs[i+1][j]:
                    count.append(j)
        return len(set(count))