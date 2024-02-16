class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        i = 0
        if len(palindrome) == 1:
            return ""
        s = list(palindrome)
        while i + 1 < len(s) and s[i] == "a":
            i += 1
        
        if i == len(s) - 1:
            s[i] = "b"
        elif len(s) % 2 != 0 and i+1 == math.ceil(len(s) / 2):
            s[len(s) - 1] = "b"
        else:
            s[i] = "a"
        
        print(i,len(s))
        return "".join(s)
        
