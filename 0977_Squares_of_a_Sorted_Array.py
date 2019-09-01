# Problem 977
# Date completed: 2019/09/01

# 268 ms
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x**2 for x in A])
