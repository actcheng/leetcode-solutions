# Problem 461
# Date completed: 2019/11/29 

# 20 ms (99%)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x == y: return 0
        if y<x: x, y = y, x # so that y>=x
        xstr, ystr = str(bin(x)).split('b')[-1], str(bin(y)).split('b')[-1]
        xstr = '0'*(len(ystr)-len(xstr)) + xstr
        return sum([xstr[i]!=ystr[i] for i in range(len(ystr))])
