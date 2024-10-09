# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = [float('inf')] * (n + 1)
        time[0] = 0
        time[k] = 0
        graph = defaultdict(list)
        for u , v ,w in times:
            graph[u].append((v,w))
        
        # print(graph)
        heap = [(0,k)]
        while heap:
            cost, node = heappop(heap)
            for new_node, new_cost in graph[node]:
                if time[new_node] > (new_cost + cost):
                    time[new_node] = new_cost + cost
                    heappush(heap,(new_cost + cost, new_node))
        # print(time)
        minTime = max(time)
        if minTime == float('inf'):
            return -1
        return minTime
