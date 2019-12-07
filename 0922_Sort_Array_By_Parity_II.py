# Problem 922
# Date completed: 2019/12/07 

# 232 ms (87%)
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        o, e = 1,0
        l = len(A)
        while o < l and e < l:
            if A[o] % 2 == 0 and A[e] % 2 == 1: # Swap
                A[o], A[e] = A[e], A[o]
                o += 2
                e += 2
            elif A[o] % 2 == 1:
                o += 2
            else:
                e += 2
                
        return A
