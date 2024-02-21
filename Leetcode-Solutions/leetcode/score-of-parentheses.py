class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i in s:
            if i == "(":
                stack.append(0)
            else:
                popped = stack.pop()
                val = max(1, 2 * popped)
                stack[-1] += val
        return stack[0]