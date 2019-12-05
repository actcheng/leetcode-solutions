# Problem 695
# Date completed: 2019/12/05 

# 132 ms (97%)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        h,w = len(grid), len(grid[0])
        self.directions = [[1,0],[-1,0],[0,1],[0,-1]]
        res = 0
        
        def BST(i,j):
            area = 1
            queue = [[i,j]]
            grid[i][j] = -1
            while queue:
                y,x = queue.pop(0)                
                for [dy,dx] in self.directions:
                    new_x, new_y = x+dx, y+dy
                    if 0 <= new_x < w and 0 <= new_y < h:
                        if grid[new_y][new_x] > 0:
                            area += 1
                            queue.append([new_y,new_x])
                        grid[new_y][new_x] = -1
            return area
            
        for i in range(h): #y
            for j in range(w): #x
                if grid[i][j] > 0:
                    res = max(res,BST(i,j))
                
        return res
