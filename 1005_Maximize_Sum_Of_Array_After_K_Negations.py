# Problem 1005
# Date completed: 2019/09/02

# 56 ms
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        # Negative first
        # Divide by two
        # Pick the smallest
        
        A.sort()
        i = 0
        k = K
        while k > 0 and A[i] < 0 and i < len(A):
            A[i] = -A[i]
            i += 1
            k -= 1
        
        if k > 0 and k % 2 > 0:
            if i>0 and A[i-1] < A[i]:
                A[i-1] = -A[i-1]
            else:
                A[i] =  -A[i]

        return sum(A)
