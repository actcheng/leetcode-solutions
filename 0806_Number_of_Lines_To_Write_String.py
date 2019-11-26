# Problem 806
# Date completed: 2019/11/26 

# 32 ms (90%)
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        if not S: return [0,0]
        a = ord('a')
        line = 0
        n = 1
        for s in S:
            line += widths[ord(s)-a]
            if line >= 100:
                n += 1                
                line = widths[ord(s)-a] if line > 100 else 0
       
        return [n, line]
