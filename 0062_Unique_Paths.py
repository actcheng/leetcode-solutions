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

# 2020/06/29
# 24 ms (94%), DP solution

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1
        
        prev_row = [1 for i in range(m)]
        this_row = [1 for i in range(m)]
        
        for i in range(1,n):
            for j in range(1,m):
                this_row[j] = prev_row[j] + this_row[j-1]
            prev_row, this_row = this_row, [1 for i in range(m)]
            
        return prev_row[-1]
