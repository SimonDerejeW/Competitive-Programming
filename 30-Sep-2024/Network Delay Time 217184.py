# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nums = [float('inf')] * (n+1)
        nums[0] = 0
        graph = defaultdict(list)
        visited = set()
        visited.add(k)

        for u , v , t in times:
            graph[u].append([v,t])
        
        que = []
        heappush(que, (0,k))

        while que:
            time, node = heappop(que)
            visited.add(node)
            nums[node] = min(nums[node],time)
            for new_node, new_time in graph[node]:
                if new_node not in visited:
                    heappush(que,(new_time + time, new_node))

        total = max(nums)
        if total == float('inf'):
            return -1
        return total
