class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = {"T": 0, "F": 0}
        left = 0
        maxCons = 0
        n = len(answerKey)

        for right in range(n):

            count[answerKey[right]] += 1

            while min(count["T"], count["F"]) > k:
                count[answerKey[left]] -= 1
                left+=1
            
            maxCons = max(maxCons, right-left+1)
        return maxCons