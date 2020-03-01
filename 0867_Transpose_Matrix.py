# Problem 867
# Date completed: 2020/03/01 

# 72 ms (80%)
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
