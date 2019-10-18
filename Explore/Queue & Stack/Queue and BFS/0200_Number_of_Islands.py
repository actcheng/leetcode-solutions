# Problem 200
# Date completed: 2019/10/18 

# 208 ms (10%)
if not grid or not grid[0]: return 0
        h, w = len(grid), len(grid[0])
        queue = [[0,0]]
        self.counter = 0
        self.islands = {}
        if grid[0][0] == "1":            
            self.counter += 1
            grid[0][0] = self.counter
            self.islands[self.counter] = [[0,0]]
        else:
            grid[0][0] = -1

        def helper(new_i,new_j):
            if type(grid[new_i][new_j]) == str : 
                queue.append([new_i,new_j])
            else:
                return
            
            if (grid[new_i][new_j] == "1"):        
                neighbor = []
                if new_i > 0: neighbor.append(grid[new_i-1][new_j])
                if new_j > 0: neighbor.append(grid[new_i][new_j-1])
                    
                if max(neighbor) == -1:
                    self.counter +=1
                    grid[new_i][new_j] = self.counter
                    self.islands[self.counter] = [[new_i,new_j]]
                else:
                    if min(neighbor) == -1 or min(neighbor)==max(neighbor):
                        grid[new_i][new_j] = max(neighbor)
                        self.islands[max(neighbor)].append([new_i,new_j])
                    else:                        
                        ind= min(neighbor) 
                        grid[new_i][new_j] = ind
                        for [i,j] in self.islands[max(neighbor)]: 
                            grid[i][j] = ind
                            
                        self.islands[ind].extend(self.islands[max(neighbor)])
                        self.islands[ind].append([new_i,new_j])
                        del self.islands[max(neighbor)]                         
            else:
                grid[new_i][new_j] = -1
        while queue:
            [i,j] = queue.pop(0)   
            if j+1<w: helper(i,j+1)
            if i+1<h: helper(i+1,j)
        
        return len(self.islands.keys())          
