# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        indegree = defaultdict(int)
        for u  ,v in edges:
            indegree[u] += 1
            indegree[v] += 1
        n = len(indegree)
        for key, val in indegree.items():
            if val == n-1:
                return key