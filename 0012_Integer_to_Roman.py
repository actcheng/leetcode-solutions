# Problem 12
# Date completed: 2019/10/06 

# 64 ms (34%)
class Solution:
    def intToRoman(self, num: int) -> str:
        syms = {1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I'}
        halves = set([500,50,5])
        res = []
        for s in syms:
            tenth = int(s*0.1) if s not in halves else int(s*0.2)
            while num >= s-tenth:
                if s-tenth<= num < s:
                    res.append(syms[tenth])
                    num += tenth
                res.append(syms[s])
                num -= s
               
        return ''.join(res)
