class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key = lambda x: x[0])
        start = points[0][0]
        end = points[0][1]
        count = 1
        for i in range(1,len(points)):
            if points[i][0] > end:
                count +=1
                end = points[i][1]
            else:
                end = min(end, points[i][1])
        return count
        