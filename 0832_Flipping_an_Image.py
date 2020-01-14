# Problem 832
# Date completed: 2020/01/14 

# 48 ms (75%)
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[1 if x==0 else 0 for x in row[::-1]] for row in A]
