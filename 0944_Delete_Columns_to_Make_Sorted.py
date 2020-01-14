# Problem 944
# Date completed: 2020/01/14 

# 176 ms (50%)
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if len(A) <= 1: return 0
        res = 0
        nrow, ncol = len(A), len(A[0])
        for i in range(ncol):
            for j in range(nrow-1):
                if A[j+1][i] < A[j][i]:
                    res += 1
                    break
        return res
