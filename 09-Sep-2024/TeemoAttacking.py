class Solution:
    def findPoisonedDuration(self, nums: List[int], duration: int) -> int:
        arr = [0] * (nums[-1] + duration + 1)
        for num in nums:
            arr[num] += 1
            arr[num + duration] -= 1

        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
        
        score = 0
        for num in arr:
            if num > 0:
                score += 1
        return score
