class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        def backtrack(start,sub):
            result.append(tuple(sub[:]))
            
            for i in range(start , len(nums)):
                sub.append(nums[i])
                backtrack(i + 1, sub)
                sub.pop()
        
        backtrack(0,[])
        
        return list(set(result))
