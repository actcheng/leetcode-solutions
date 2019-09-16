# Problem 661 
# Date completed: 2019/09/16

# 636 ms
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        if not M: return 
        from math import floor
        origM = [[i for i in row] for row in M]
        h = len(M)
        w = len(M[0])
        
        for i in range(h):
            min_i = max(0,i-1)
            max_i = min(h-1,i+1)+1
            for j in range(w):
                min_j = max(0,j-1)
                max_j = min(w-1,j+1)+1      
                sumArea = sum([sum(row[min_j:max_j]) for row in origM[min_i:max_i]])
                M[i][j] = floor(sumArea/((max_j-min_j)*(max_i-min_i)))
                
                # print(min_i,max_i,min_j,max_j,sumArea/((max_j-min_j)*(max_i-min_i)))
                # print([row[min_j:max_j] for row in origM[min_i:max_i]],M[i][j])
                
        return M
