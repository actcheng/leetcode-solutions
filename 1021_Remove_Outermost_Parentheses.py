# Problem 1021
# Date completed: 2019/12/18 

# 28 ms (98%)
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ""
        prim = ""
        order = 0
        
        for c in S:
            if c == "(":
                if order > 0:
                    res+=c
                order += 1
            if c == ")":
                if order > 1:
                    res += c
                order -= 1
                
        return res
