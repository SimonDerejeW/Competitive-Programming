class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()

        def backtrack(perms):
            if sum(perms) == target:
                result.add(tuple(sorted(perms[:])))
                return
            if sum(perms) > target:
                return
            
            for i in range(len(candidates)):
                perms.append(candidates[i])
                backtrack(perms)
                perms.pop()
        
        backtrack([])

        return list(result)