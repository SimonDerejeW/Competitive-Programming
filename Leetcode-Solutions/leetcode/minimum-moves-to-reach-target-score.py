class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target > 1:
            if target % 2 == 0 and maxDoubles:
                target = target // 2
                maxDoubles -= 1
            elif target % 2 != 0 and maxDoubles:
                target -= 1
            elif maxDoubles == 0:
                count += (target - 1)
                break
            count += 1
        
        return count