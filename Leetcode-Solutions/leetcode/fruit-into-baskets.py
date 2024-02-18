class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        l = 0
        maxSub = 1

        for r in range(len(fruits)):
            count[fruits[r]] = 1 + count.get(fruits[r], 0)
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    count.pop(fruits[l])
                l += 1
            maxSub = max(maxSub,r-l+1)
            

        return maxSub
            