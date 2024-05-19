# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        seen = {}
        start = ord("a")
        for i in range(26):
            seen[chr(start + i)] = 1 << i

        bitted = []
        for i in range(len(words)):
            bit_val = 0
            for char in words[i]:
                bit_val |= seen[char]
            bitted.append(bit_val)

        maxLen = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bitted[i] & bitted[j] == 0:
                    maxLen = max(maxLen, (len(words[i]) * len(words[j])))
        return maxLen
