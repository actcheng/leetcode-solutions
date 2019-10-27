# Problem 841
# Date completed: 2019/10/27 

# 76 ms (80%)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*len(rooms)
        queue = [[0]]
        while queue:
            keys = queue.pop(0)
            for key in keys:
                if not visited[key]:
                    queue.append(rooms[key])
                    visited[key] = True
        return all(visited)
