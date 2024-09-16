# Problem: Find-the-prefix-common-array-of-two-arrays - https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        def counter(seen):
            count = 0
            for key in seen:
                if seen[key] > 1:
                    count += 1
            return count

        seen = defaultdict(int)
        result = []
        for i in range(len(A)):
            seen[A[i]] += 1
            seen[B[i]] += 1
            result.append(counter(seen))
        return result

