# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u , v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        color = [-1] * (n+1)
        res = True

        def dfs(node, graph):
            temp = True
            
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    temp = temp and dfs(neighbor,graph)
                else:
                    if color[neighbor] == color[node]:
                        temp = False
                
            return temp

        for node in range(1,n+1):
            if color[node] == -1:
                color[node] = 0
            res = res and dfs(node , graph)
            
        return res