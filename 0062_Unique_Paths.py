# Problem 62
# Date completed: 2019/10/13 

# 36 ms (77%)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 0
        paths = collections.defaultdict(int)
        paths[(0,0)] = 1
        queue = [(0,0)]
        
        def helper(next_loc,num):               
            if next_loc not in paths: queue.append(next_loc)
            paths[next_loc] += num
            
        while queue:
            loc = queue.pop(0)
            if loc[0]+1 < m: helper((loc[0]+1, loc[1]  ), paths[loc])
            if loc[1]+1 < n: helper((loc[0]  , loc[1]+1), paths[loc])    
                
        return paths[m-1,n-1]
