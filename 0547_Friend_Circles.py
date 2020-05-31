# Problem 547
# Date completed: 2020/06/01 

# 220 ms (38%)
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        l = len(M) 
        parent = [i for i in range(l)]
        
        find = lambda i: i if parent[i]==i else find(parent[i])
        
        for i in range(l):
            for j in range(l):
                if M[i][j] == 1:
                    x, y = find(i), find(j)
                    if x != y:
                        parent[y] = x
                    
        return len([i for i in range(l) if i==parent[i]])
