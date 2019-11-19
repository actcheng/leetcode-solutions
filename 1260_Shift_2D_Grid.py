# Problem 1260
# Date completed: 2019/11/19 

# 164 ms (86%)
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not grid or not grid[0]: return grid
        
        h, w = len(grid), len(grid[0])
        spread = [x for row in grid for x in row] 
        n = h*w - k % (h*w)
        spread = spread[n:] + spread[:n]
        return [spread[i*w:(i+1)*w] for i in range(h)]
