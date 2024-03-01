class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = set()
        nums = list(range(1 , 10))
        def backtrack(i , summ, perms):
            if len(perms) == k:
                if summ == n:
                    res.add(tuple(perms[:]))
                return

            if i >= len(nums) or summ > n:
                return
            
            summ += nums[i]
            perms.append(nums[i])
            backtrack(i + 1,summ,perms)

            summ -= perms.pop()
            backtrack(i + 1, summ,perms)
        
        backtrack(0, 0 , [])
        return list(res)



                