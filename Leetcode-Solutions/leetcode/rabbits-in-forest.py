class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = defaultdict(int)
        number = 0
        for i in answers:
            rabbits[i] += 1
        
        for i in rabbits:
            x = math.ceil(rabbits[i]/(i+1))
            number += x * (i+1)
        
        return number

