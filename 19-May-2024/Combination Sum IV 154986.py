# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1,len(dp)):
            for num in nums:
                if i - num > -1:
                    dp[i] += dp[i-num]
        # print(dp)
        return dp[target]