# Problem 463 
# Date completed: 2019/09/18

# 672 ms
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        
        h, w = len(grid), len(grid[0])
        islands = [[i,j] for i in range(h) for j in range(w) if grid[i][j]==1 ]
        
        self.perimeter = len(islands)*4
        
        def helper(i,j):
            if grid[i][j]==1: self.perimeter -= 1
                
        for [i,j] in islands:
            if i>0: helper(i-1,j)
            if j>0: helper(i,j-1)
            if i<h-1: helper(i+1,j)
            if j<w-1: helper(i,j+1)
            # print(i,j,self.perimeter)
                
        return self.perimeter
        
