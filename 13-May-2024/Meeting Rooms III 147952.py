# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = defaultdict(int)
        m = 0
        meetings.sort()
        # print(meetings)
        heap = []
        minHeap = list(range(0 , n))

        for start, end in meetings:
            while heap and heap[0][0] <= start:
                # print('1: ', (start , end))
                x , y = heappop(heap)
                heappush(minHeap , y)
            if minHeap:
                m = heappop(minHeap)
                heappush(heap , (end , m))
                # print('2: ', (start , end, m))
                rooms[m] += 1
                # m += 1
            else:
                x , y = heappop(heap)
                heappush(heap , (end + x - start , y))
                rooms[y] += 1
                # print('3: ', (start , end, y))
        # print(rooms)
        new = sorted(rooms.items(), key = lambda x : (x[1] , -x[0]), reverse = True)

        return new[0][0]

