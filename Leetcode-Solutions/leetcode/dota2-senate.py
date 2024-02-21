class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        counter = Counter(senate)
        queue = deque(senate)
        r = 0
        d = 0
        while counter["R"] != 0 and counter["D"] != 0 :
            if queue[0] == "D" and d >= 0:
                counter["R"] -= 1
                r -= 1
                queue.append(queue.popleft())
            elif queue[0] == "D" and d < 0:
                d += 1
                queue.popleft()
            elif queue[0] == "R" and r >= 0:
                counter["D"] -= 1
                d -= 1
                queue.append(queue.popleft())
            elif queue[0] == "R" and r < 0:
                r += 1
                queue.popleft()
    
        if counter["R"] == 0:
            return "Dire"
        else:
            return "Radiant"
            



