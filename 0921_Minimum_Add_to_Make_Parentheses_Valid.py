# Problem 921
# Date completed: 2020/01/07 

# 32 ms (32%)
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        o = 0
        res = 0
        for x in S:
            if x == '(':
                o+= 1
            else:
                if o == 0:
                    res += 1
                else:
                    o -= 1
        return o+res

