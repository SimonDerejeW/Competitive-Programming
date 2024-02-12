class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        seen = {}
        vowel = "aeiou"
        maxVowel = left = 0

        for i in range(k):
            if s[i] in vowel:
                seen[s[i]] = 1 + seen.get(s[i],0)

        maxVowel = max(maxVowel, sum(seen.values()))

        for right in range(k, len(s)):
            if s[right] in vowel:
                seen[s[right]] = 1 + seen.get(s[right],0)
            
            if s[left] in vowel:
                seen[s[left]] -= 1
            left += 1

            maxVowel = max(maxVowel, sum(seen.values()))

        return maxVowel



        