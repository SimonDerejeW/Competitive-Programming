# Problem: All Paths From Source to Target - https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        def dfs(node,curr):
            curr.append(node)
            if node == len(graph) - 1:
                result.append(curr[:])
                return
            
            for num in graph[node]:
                dfs(num,curr[:])
        
        dfs(0,[])
        return result
