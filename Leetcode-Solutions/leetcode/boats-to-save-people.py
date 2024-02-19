class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        right = len(people) - 1
        left = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                boats += 1
            else:
                right -= 1
                boats += 1
        return boats




        