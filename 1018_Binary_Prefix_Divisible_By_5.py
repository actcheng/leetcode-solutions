# Problem 1018
# Date completed: 2019/12/27 

# 304 ms (67%)
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        num = 0
        for x in A:
            num = (num<<1)+x
            res.append(num%5==0)
        return res
