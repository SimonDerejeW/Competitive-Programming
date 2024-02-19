class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # lis = []
        # for i in range(len(temperatures)):
        #     count = -1
            
        #     for j in range(i,len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             count+=1
        #             lis.append(count)
        #             break
        #         else:
        #             count+=1
        #             j+=1
        # return lis


        stack = []
        res = [0] * len(temperatures)
        
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                res[j] = i-j
            stack.append(i)
            
        return res
                
                
                