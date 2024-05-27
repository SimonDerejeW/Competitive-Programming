# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        left = 0
        seen = defaultdict(int)
        count = 0

        for right in range(len(s)):
            seen[s[right]] += 1
            temp = left
            if len(seen) < right - left + 1:
                seen = defaultdict(int)
                left = right
                seen[s[right]] += 1
            if temp != left:
                count += 1
        return count + 1