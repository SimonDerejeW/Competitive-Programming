class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        k = len(nums)
        def backtrack(perm): 
            if len(perm) == k:
                perms.append(perm[:])
            
            for i in range(len(nums)):
                if nums[i] not in perm:
                    perm.append(nums[i])
                    backtrack(perm)
                    perm.pop()
            
        backtrack([])
        return perms