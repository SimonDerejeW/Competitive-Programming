class Solution:
    def maxScore(self, s: str) -> int:
        nums = list(map(int, list(s)))
        score = 0
        hashmap = Counter(nums)
        zeroCount = 0

        for i in range(len(nums)-1):
            if nums[i] == 0:
                zeroCount += 1
            else:
                hashmap[1]-=1
            score = max(score , hashmap[1] + zeroCount)
        return score
