# Problem: Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        subsets = []
        def backtrack(idx, sub):
            if idx >= len(nums):
                subsets.append(sub[:])
                return
            
            sub.append(nums[idx])
            backtrack(idx + 1, sub)
            sub.pop()
            backtrack(idx + 1, sub)
        backtrack(0,[])

        ans = []
        for i in range(len(subsets)):
            res = 0
            for num in subsets[i]:
                res |= num
            ans.append(res)
        ans.sort(reverse=True)
        return ans.count(ans[0])
