# Problem 6
# Date completed: 2019/09/26 

# 60 ms
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        rows = [[] for i in range(numRows)]
        gp = 2*numRows -2
        for i in range(len(s)):
            ind = i % gp
            if ind <numRows:
                rows[ind].append(s[i])
            else:
                rows[gp-ind].append(s[i])
        
        return ''.join([x for row in rows for x in row ])
