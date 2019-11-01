# Problem 64
# Date completed: 2019/11/01 

# 160 ms (7%)
# BFS
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return None
        h,w = len(grid), len(grid[0])
        minSum = [False]*w*h
        directions = [[0,1],[1,0]]
        queue = [[0,0]]
        minSum[0] = grid[0][0]
        while queue:
            x,y = queue.pop(0)
#             print(x,y)
            for inc in directions:
                new_x, new_y = x+inc[0], y+inc[1]
                if new_x < w and new_y<h:
                    if not minSum[new_y*w+new_x]:
                        minSum[new_y*w+new_x] = minSum[y*w+x] + grid[new_y][new_x]
                        queue.append([new_x,new_y])
                    else:
                        minSum[new_y*w+new_x] =min(minSum[new_y*w+new_x],
                                                  minSum[y*w+x] + grid[new_y][new_x])
        
        return minSum[-1]
