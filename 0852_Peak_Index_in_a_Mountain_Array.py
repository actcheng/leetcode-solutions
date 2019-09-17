# Problem 852 
# Date completed: 2019/09/17

# 92 ms
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int: 
        return A.index(max(A))
