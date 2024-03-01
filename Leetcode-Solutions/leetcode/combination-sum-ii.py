class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def backtrack(i , combs, summ):
            if summ == target:
                res.add(tuple(combs[:]))
                return
            
            if i >= len(candidates) or summ > target:
                return
            
            summ += candidates[i]
            combs.append(candidates[i])
            backtrack(i + 1,combs,summ)

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            summ -= combs.pop()
            backtrack(i + 1, combs,summ)
        backtrack(0,[],0)
        return list(res)
