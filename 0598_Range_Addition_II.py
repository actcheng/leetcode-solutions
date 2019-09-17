# Problem 598 
# Date completed: 2019/09/17

# 84 ms
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops: return m*n
        min_i = min([x[0] for x in ops])
        min_j = min([x[1] for x in ops]) 
        return min_i*min_j
