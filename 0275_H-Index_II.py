# Problem 275
# Date completed: 2020/06/18

# 152 ms, 54 %
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        l = len(citations)
        for i in range(1,l+1):
            if citations[l-i] < i:
                return i-1
        return i 
