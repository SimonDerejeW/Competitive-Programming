# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        perms = []
        n = len(s)
        def backtrack(idx,perm):
            if len(perm) == n:
                y = perm[:]
                x = "".join(y)
                perms.append(x)
                return
            if idx >= n:
                return
            
            if s[idx].isalpha():
                # perm.append(s[idx].upper())
                backtrack(idx + 1 , perm + [s[idx].upper()])
                # perm.pop()
                # perm.append(s[idx].lower())
                backtrack(idx + 1 , perm + [s[idx].lower()])
            else:
                # perm.append(s[idx])
                backtrack(idx + 1 , perm + [s[idx]])
        backtrack(0,[])
        return perms
