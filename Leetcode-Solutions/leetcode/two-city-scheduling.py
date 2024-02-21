class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        def profit(arr):
            return arr[1] - arr[0]
        
        costs.sort(key = lambda x: x[1] - x[0])
        
        maxProfit = 0
        for i in range(len(costs)):
            if i < (len(costs)//2):
                maxProfit += costs[i][1]
            else:
                maxProfit += costs[i][0]
        
        return maxProfit


