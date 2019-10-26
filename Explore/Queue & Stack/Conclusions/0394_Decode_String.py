# Problem 394
# Date completed: 2019/10/26 

# 40 ms (30%)
class Solution:
    def decodeString(self, s: str) -> str:
#         print('s',s)
        res = []
        num_str = []
        stack = []
        code = []
        num = 1
        for x in s:
            if x.isnumeric():
                if len(stack)==0:
                    num_str.append(x)
                else:
                    code.append(x)
            elif x == '[':                
                if len(stack) == 0:
                    num = int(''.join(num_str)) if num_str else 1
                    num_str = []
#                     print(num)
                else:
                    code.append(x)
                stack.append('[')                
            elif x == ']':
                stack.pop()
                if len(stack) > 0:                    
                    code.append(x)
                else:
#                     print('code',code)
                    res.append(num*self.decodeString(''.join(code)))
                    code = []
#                     print('res',res)
            elif len(stack) > 0:
                code.append(x)
            else:
                res.append(x)
                
        return ''.join(res)
