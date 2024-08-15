# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        profit = defaultdict(int)
        for bill in bills:
            if bill == 5:
                profit[5] += 1
            elif bill == 10 and profit[5] >= 1:
                profit[10] += 1
                profit[5] -= 1
            elif bill == 20 and (profit[10] >= 1 and profit[5] >= 1):
                profit[20] += 1
                profit[10] -= 1
                profit[5] -= 1
            elif bill == 20 and profit[5] >= 3:
                profit[5] -= 3 
            else:
                return False
        return True

