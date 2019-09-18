# Problem 994 
# Date completed: 2019/09/18

# 68 ms
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return     
        
        self.fresh = sum([row.count(1) for row in grid])
        if self.fresh == 0: return 0
        
        w = len(grid[0])
        h = len(grid)        
        
        rotten = [[i,j] for i in range(h) for j in range(w) if grid[i][j] == 2]
        new_rotten = []
        
        def helper(i,j):
            if grid[i][j] == 1:
                grid[i][j] = 2
                new_rotten.append([i,j])  
                self.fresh -= 1
        
        time = 0
        while rotten:
            i,j = rotten.pop(0)
            if i>0: helper(i-1,j)
            if j>0: helper(i,j-1)
            if i<h-1: helper(i+1,j)
            if j<w-1: helper(i,j+1)
            
            # print(grid)
            # print(new_rotten,rotten,self.fresh)
            
            if not rotten:
                rotten = list(new_rotten)
                new_rotten = []
                time += 1
                if self.fresh<=0: return time
                
        return -1
