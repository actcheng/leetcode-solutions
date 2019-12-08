# Problem 868
# Date completed: 2019/12/08 

# 24 ms (96%)
class Solution:
    def binaryGap(self, N: int) -> int:
        s = bin(N).split('b')[-1]
        r = 0
        l = -1
        for c in s: 
            if l>=0: l += 1
            if c == '1':
                r = max(l,r)
                l = 0
        return r
