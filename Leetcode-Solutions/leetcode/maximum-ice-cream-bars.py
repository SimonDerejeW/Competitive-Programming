class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ice = 0
        for i in costs:
            if i <= coins:
                ice += 1
                coins -= i
            else:
                break
        return ice

