# Problem 696 
# Date completed: 2019/09/16

# 292 ms
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if s == "": return 1
        arr = [int(c) for c in s]
        total = 0
        counts = [0,0]
        state = None
        for c in arr: 
            if state == None:                 
                counts[c] = 1
            elif c == state:
                counts[c] += 1
            else:
                total += min(counts)
                counts[c] = 1
            state = c
            
        total += min(counts)
        return total   
                
