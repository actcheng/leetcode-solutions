# Problem 1249
# Date completed: 2020/01/19 

# 128 ms (65%)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        po = []
        pc = []
        for i in range(len(s)):
            if s[i] == '(':
                po.append(i)
            elif s[i] == ')':
                if po:
                    po.pop()
                else:
                    pc.append(i)
        res = ''   
        removes = set(po+pc)
        for i in range(len(s)):
            if i not in removes:
                res += s[i]
        return res
