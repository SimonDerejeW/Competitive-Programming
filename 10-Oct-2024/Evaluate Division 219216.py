# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1 / values[i]))

        def bfs(src,target):
            if src not in graph or target not in graph:
                return -1
            que = deque()
            visited = set([src])
            que.append((src, 1))
            
            while que:
                node, cost = que.popleft()
                if node == target:
                    return cost
                for new_node, new_cost in graph[node]:
                    if new_node not in visited:
                        visited.add(new_node)
                        que.append((new_node, cost * new_cost))
            return -1


        result = []
        for a, b in queries:
            result.append(bfs(a,b))
        return result
