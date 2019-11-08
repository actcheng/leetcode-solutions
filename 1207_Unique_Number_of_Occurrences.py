# Problem 1207
# Date completed: 2019/11/08 

# 32 ms (99%)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = list(collections.Counter(arr).values())
        return len(counts) == len(set(counts))
        
