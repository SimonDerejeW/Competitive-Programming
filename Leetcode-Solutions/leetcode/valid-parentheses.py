class Solution:
    def isValid(self, s: str) -> bool:
        par = {"(": ")", "{": "}", "[":"]"}
        stack = []
        for i in s:
            if i in par:
                stack.append(i)
            else:
                if not stack or i != par[stack.pop()]:
                    return False
                
        if len(stack) == 0:
            return True
        return False
