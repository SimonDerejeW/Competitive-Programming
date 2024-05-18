# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        n = len(s)
        memo = {}

        def isPalindrome(s,i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dp(i):
            if i >= n:
                res.append(part[:])
                return
            
            for j in range(i , n):
                if (i , j) not in memo:
                    pal = isPalindrome(s , i , j)
                    memo[(i , j)] = pal
                else:
                    pal = memo[(i , j)]
                if pal:
                    part.append(s[i:j+1])
                    dp(j+1)
                    part.pop()
        dp(0)
        return res

