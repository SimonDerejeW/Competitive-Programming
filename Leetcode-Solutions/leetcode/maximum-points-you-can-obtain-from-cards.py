class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window  = n - k
        total = sum(cardPoints)
        score = 0
        summ,left = 0,0
        for i in range(window):
            summ += cardPoints[i]
        score = max(score , total - summ)
        for right in range(window,n):
            summ -= cardPoints[left]
            summ += cardPoints[right]
            left += 1
            score = max(score , total - summ)

        return score
        


