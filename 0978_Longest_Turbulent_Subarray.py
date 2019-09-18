# Problem 978 
# Date completed: 2019/09/18

# 584 ms
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if not A: return
        if len(A) == 1 or max(A)==min(A): return 1
        
        signs = [A[i]>A[i+1] for i in range(len(A)-1)]
        maxSize = 0
        size = 0
        for i in range(len(signs)-1):
            if signs[i] != signs[i+1] and A[i]!=A[i+1] and A[i+1]!=A[i+2]:
                size +=1
            else:
                size = 0
            maxSize = max(size,maxSize)
        return maxSize+2
