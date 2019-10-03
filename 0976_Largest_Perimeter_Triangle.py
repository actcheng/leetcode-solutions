# Problem 976
# Date completed: 2019/10/03 

# 188 ms (27%)
class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)<3: return 0        
        A.sort(reverse=True)
        for i in range(len(A)-2):
            if A[i] < A[i+1]+A[i+2]:
                return sum(A[i:i+3])            
        return 0
        
