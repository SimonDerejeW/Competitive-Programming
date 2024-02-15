class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""
        for i in s:
             if i.isalnum():
                 pal+=i
        pal = pal.lower()
        lis = list(pal)
        if lis[::]==lis[::-1]:
            return True
        else:
            return False