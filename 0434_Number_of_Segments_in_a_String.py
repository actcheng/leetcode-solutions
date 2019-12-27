# Problem 434
# Date completed: 2019/12/27 

# 24 ms (91%)
class Solution:
    def countSegments(self, s: str) -> int:
        if not s: return 0
        res = 0 
        seg = False
        for c in s:
            if c == ' ':
                if seg: res += 1
                seg = False
            else:
                seg = True
        if seg: res += 1
        return res
