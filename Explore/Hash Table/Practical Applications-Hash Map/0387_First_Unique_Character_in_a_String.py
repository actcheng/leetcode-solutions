# Problem 387
# Date completed: 2019/09/21

# 72 ms
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        c = Counter(list(s))
        ind = [s.index(x) for x in c if c[x]==1]
        if not ind: 
            return -1
        else:
            return min(ind)
