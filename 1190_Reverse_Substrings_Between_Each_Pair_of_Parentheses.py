# Problem 1190 
# Date completed: 2019/09/15

# 48 ms
class Solution:
    def reverseParentheses(self, s: str) -> str:
        if not s: return []
        
        s = list(s)
        
        if s[-1] == '!': 
            rev = True
            s.pop()
        else: 
            rev = False
            
        front, middle, back = [], [], []
        start, end = False, False
        while not start and s:
            c = s.pop(0)
            if c != '(':
                front.append(c)
            else:
                start = True
        
        if not start: 
            if rev: 
                front.reverse()
                # print('Reversed:', front)  
            return ''.join(front)
        
        if start:
            stack = []
            while not end and s:
                c = s.pop(0)
                if c == '(':
                    stack.append(c)
                    middle.append(c)
                elif c == ')':
                    if len(stack) >0:
                        stack.pop(0)
                        middle.append(c)
                    else:
                        end = True
                else:
                    middle.append(c)
        back = s
        # print(rev, front, middle, back)

        if start and end: middle.append('!')
        # print(rev, front, middle, back)
        front = list(self.reverseParentheses(''.join(front)))
        middle = list(self.reverseParentheses(''.join(middle)))
        back = list(self.reverseParentheses(''.join(back)))
        
        if rev:            
            front.reverse()
            back.reverse()
            middle.reverse()
            # print('Reversed', back, middle, front)
            return ''.join(back+middle+front)
        
        # print(rev, front, middle, back)
        return ''.join(front+middle+back)
