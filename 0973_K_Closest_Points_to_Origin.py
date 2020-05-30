# Problem 973
# Date completed: 2020/05/30 

# 692 ms (80%)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance = [(i, p[0]**2 + p[1]**2) for i, p in enumerate(points)]
        return [points[i] for i,p in sorted(distance,key=lambda dis:dis[1])[:K]]
