# Problem 207
# Date completed: 2020/05/30 

# 168 ms (30%)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(set) 
        for edge in prerequisites:
            self.graph[edge[1]].add(edge[0])
        
        self.V = [False]*numCourses
        
        def dfs(at,path):
            # Return False if a loop is found
            self.V[at] = True
            if len(self.graph[at]) == 0: return True
            path = path.union(set([at]))
            for to in self.graph[at]:
                if to in path or (not self.V[to] and not dfs(to,path)): return False                    
            return True
        
        for at in range(numCourses):           
            if not self.V[at] and not dfs(at,set([])): return False
            
        return True   
