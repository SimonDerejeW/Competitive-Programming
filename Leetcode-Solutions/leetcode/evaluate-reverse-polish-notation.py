class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # def operations(op):
        #     temp = stack[-1] + stack[-2]
        #     stack.pop()
        #     stack[-1] = temp
        for i in tokens:
            if i == "+":
                temp = stack[-2] + stack[-1]
                stack.pop()
                stack[-1] = temp
            elif i == "-":
                temp = stack[-2] - stack[-1]
                stack.pop()
                stack[-1] = temp
            elif i == "*":
                temp = stack[-1] * stack[-2]
                stack.pop()
                stack[-1] = temp
            elif i == "/":
                temp = stack[-2] / stack[-1]
                stack.pop()
                if temp > 0:
                    temp = math.floor(temp)
                else:
                    temp = math.ceil(temp)
                stack[-1] = temp
            else:
                stack.append(int(i))
    
        return stack[0]
                
