# Problem 389
# Date completed: 2019/12/24 

# 28ms (95%)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts_s = collections.Counter(s)
        counts_t = collections.Counter(t)
        
        for c in counts_t:
            if c not in counts_s or counts_t[c]>counts_s[c]:
                return c
