class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])

        # i = 1
        first = points[0][1]
        arrows = 1
        print(first)
        for i in range(1,len(points)):
            if first >= points[i][0]:
                continue
            else:
                first = points[i][1]
                arrows += 1

        return arrows



        
