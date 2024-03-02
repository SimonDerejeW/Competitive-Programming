class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # ###Brute Force

        # res = []
        # k = 0
        # str1 = [s[i]]
        # for i in range(len(s)):
        #     str1 = [s[i]]
        #     for j in range(i + 1, len(s)):
        #         if s[j] == s[i].lower() or s[j] == s[i].upper():
        #             str1.append(s[j])
        #         else:
        #             break
        #     if len(str1) > 1 and len(str1) > len(res):
        #         res = str1
        
        # return "".join(res)

        if len(s) < 2:
            return ""

        s_set = set(s)
        for i,c in enumerate(s):
            if c.swapcase() not in s_set:
                s1 = self.longestNiceSubstring(s[0:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                return s2 if len(s2) > len(s1) else s1
        return s


