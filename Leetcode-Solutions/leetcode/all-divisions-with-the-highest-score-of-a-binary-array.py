class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zero = 0
        one = nums.count(1)
        res = {}

        for i in range(len(nums)):
            res[i] = zero + one
            if nums[i] == 0:
                zero += 1
            else:
                one -= 1
        res[len(nums)] = zero
        
        score = max(res.values())
        ans = []
        for key in res:
            if res[key] == score:
                ans.append(key)
        return ans
