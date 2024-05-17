# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            calc = questions[i][0]
            if i + questions[i][1] + 1 < n:
                calc += dp[i + questions[i][1] + 1]

            if i + 1 < n:
                dp[i] = max(calc, dp[i + 1])
            else:
                dp[i] = calc

        return dp[0]
