class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = "()"
        permutations = []

        def backtrack(perms):
            if len(perms) == 2 * n:
                permutations.append("".join(perms[:]))
                # print(permutations)
                return
            
            for i in range(len(s)):
                # if s[i] not in perms:
                perms.append(s[i])
                backtrack(perms)
                perms.pop()
        
        backtrack([])

        def validPar(perms):
            stack = []
            for char in perms:
                if stack and stack[-1] == "(" and char == ")":
                    stack.pop()
                else:
                    stack.append(char)
            return len(stack) == 0
        
        validPerms = []
        for i in permutations:
            if validPar(i):
                validPerms.append(i)

        
        return validPerms
        
