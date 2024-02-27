class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(idx, sub):
            if len(sub) > 0:
                result.append(sub[:])
            
            for i in range(idx, len(nums)):
                sub.append(nums[i])
                backtrack(i + 1,sub)
                sub.pop()
        
        backtrack(0,[])
        result.append([])
        return result


                