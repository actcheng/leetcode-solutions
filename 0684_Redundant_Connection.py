# Problem 684
# Date completed: 2020/06/01 

# 48 ms (97%)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n)]
        find = lambda i: i if parent[i] == i else find(parent[i])
        
        res = edges[0]
        for edge in edges:
            x, y = find(edge[0]-1), find(edge[1]-1)
            if x == y:
                res = edge
            else:
                parent[y] = x
                
        return res
