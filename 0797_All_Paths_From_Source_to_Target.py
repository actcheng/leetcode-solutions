# Problem 797
# Date completed: 2020/07/24 

# 104 ms (87%)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        des = len(graph)-1
        def dfs(path,current):
            new_path = path + [current]
            if current == des:
                res.append(new_path)
            else:                
                for to in graph[current]:
                    dfs(new_path,to)
                    
            return
        
        dfs([],0)
        return res
