# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # graph = defaultdict(list)
        incoming = [0 for _ in range(n)]
        for u , v in edges:
            incoming[v] += 1
        result = []
        for i in range(len(incoming)):
            if incoming[i] == 0:
                result.append(i)
        return result