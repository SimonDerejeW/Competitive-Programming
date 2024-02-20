class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        nextSmaller = [(len(arr))] * len(arr)
        prevSmaller = [-1] * len(arr)

        minSum = 0
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                x = stack.pop()
                nextSmaller[x] = i 
            
            if stack:
                prevSmaller[i] = stack[-1]
            
            stack.append(i)
        
        for i in range(len(arr)):
            minSum += (arr[i] * ((nextSmaller[i] - i) * (i - prevSmaller[i])))
            # print(nextSmaller[i] - i , i - prevSmaller[i])
            
        
        # print(nextSmaller)
        # print(prevSmaller)
        return minSum % (10 ** 9 + 7)
