# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        parents = {i:i for i in range(n)}
        rank = defaultdict(int)

        def find(x):
        # Write your code here
            if x == parents[x]:
                return x
            par = find(parents[x])
            parents[x] = par
            return par
        
        def union(x, y):
        # Write your code here
            x = find(x)
            y = find(y)

            if x != y:
                if rank[x] > rank[y]:
                    parents[y] = x
                elif rank[x] < rank[y]:
                    parents[x] = y
                else:
                    parents[x] = y
                    rank[y] += 1
        
        visited = set()
        secret = set()
        secret.add(0)
        secret.add(firstPerson)
        union(firstPerson, 0)
        meetings.sort(key = lambda x : x[2])

        time = meetings[0][2]

        i , j = 0 , 0

        while i < len(meetings):

            while j < len(meetings) and time == meetings[j][2]:
                union(meetings[j][0] , meetings[j][1])
                j+=1

            j = i
            og = find(0)
            while j < len(meetings) and time == meetings[j][2]:
                if find(meetings[j][0]) != og:
                    parents[meetings[j][0]] = meetings[j][0]
                    parents[meetings[j][1]] = meetings[j][1]
                else:
                    secret.add(meetings[j][1])
                    secret.add(meetings[j][0])
                j+=1
            
            if j < len(meetings):
                time = meetings[j][2]
            else:
                time = meetings[j-1][2]
            i = j


        return list(secret)

