class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = Counter(s)
        longest = 0
        odd = 0
        for i in seen:
            longest += seen[i] - (seen[i] % 2)
            if seen[i] %2 != 0:
                odd += 1
        
        if odd > 0:
            return longest + 1
        else:
            return longest
        