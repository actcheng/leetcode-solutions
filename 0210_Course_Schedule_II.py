# Problem 210
# Date completed: 2020/07/18

# 100 ms (91%)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        edges = collections.defaultdict(list)
        for p in prerequisites:
            edges[p[1]].append(p[0])
        
        res = []
        visited = [False for i in range(numCourses)]
        path = [False for i in range(numCourses)]
        
        def dfs(i):
            visited[i] = True
            path[i] = True
            for j in edges[i]:
                if path[j]: return False
                
                if not visited[j]: 
                    if not dfs(j): return False                    
            
            path[i] = False
            res.insert(0,i)
            
            return True
        
        for i in range(numCourses):
            if not visited[i]: 
                if not dfs(i): return []
                
        return res
