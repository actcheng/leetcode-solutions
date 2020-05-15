# Problem 918
# Date completed: 2020/05/15 

# 676 ms (33%)

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        global_max = A[0]        
        n = len(A)
        
        # 1-interval
        max1 = A[0]
        for i in range(1,n):
            max1 = A[i] + max(max1,0) 
            global_max = max(global_max,max1)
        
        # 2-interval
        sum_left,sum_right = A.copy(), A.copy()
        max_right = [A[-1]]*n
        for i in range(1,n):
            sum_left[i] += sum_left[i-1]
            
        for i in range(n-2,-1,-1):            
            sum_right[i] += sum_right[i+1]
            max_right[i] = max(sum_right[i],max_right[i+1])
            global_max = max(global_max,sum_left[i]+max_right[i+1])        

        return global_max
    

