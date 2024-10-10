# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph = defaultdict(list)
        visited = set()
        visited.add(start_node)
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].append([v, succProb[i]])
            graph[v].append([u, succProb[i]])

        que = []
        heappush(que, (-1, start_node))

        while que:
            prob, node = heappop(que)
            visited.add(node)

            if node == end_node:
                return prob * -1
                
            for x, y in graph[node]:
                if x not in visited:
                    heappush(que, ((prob * y), x))

        return 0
