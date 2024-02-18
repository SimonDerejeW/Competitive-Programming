class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        if len(piles) == 3:
            return piles[1]
        
        max_coins = 0
        for i in range(1,len(piles)-int(len(piles)/3),2):
            
            max_coins += piles[i]
        return max_coins