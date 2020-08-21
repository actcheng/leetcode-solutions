# Problem 274
# Date completed: 2020/08/11

# 40 ms (37%)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        citations.sort()
        l = len(citations)
        for i in range(1,l+1):
            if citations[l-i] < i:
                return i-1
            
        return l
            
