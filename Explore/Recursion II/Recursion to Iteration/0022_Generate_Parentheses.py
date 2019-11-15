# Problem 22
# Date completed: 2019/11/15 

# 44 ms (47%)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return [""]
        res = []
        stack = [('(',n-1,n)]
        while stack:
            par, left, right = stack.pop()
            if left==0: 
                res.append(par+')'*right)
            else:                
                if right>left:
                    stack.append((par+')',left,right-1))
                stack.append((par+'(',left-1,right))
        return res
        
