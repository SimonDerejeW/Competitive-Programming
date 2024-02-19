class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = {}
        left = 0
        maxSub = 0

        for right in range(n):
            count[s[right]] = 1 + count.get(s[right] , 0)

            mostCount = max(count.values())
            
            minCount = right - left + 1 - mostCount

            while minCount > k:
                count[s[left]] -= 1
                left += 1
                minCount = right - left + 1 - max(count.values())
            
            maxSub = max(maxSub, right - left + 1)
        
        return maxSub
