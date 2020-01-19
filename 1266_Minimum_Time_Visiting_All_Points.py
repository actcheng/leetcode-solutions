# Problem 1266
# Date completed: 2020/01/19 

# 52 ms (94%)
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1,len(points)):
            dx, dy = abs(points[i][0]-(points[i-1][0])), abs(points[i][1]-(points[i-1][1]))
            time += min(dx,dy) + abs(dx-dy)
        return time
