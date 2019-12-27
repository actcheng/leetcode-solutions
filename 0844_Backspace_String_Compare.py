# Problem 844
# Date completed: 2019/12/27 

# 24 ms (95%)
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def realString(string):
            stack = []
            for c in string:
                if c == '#':
                    if stack: stack.pop()
                else:
                    stack.append(c)
            return ''.join(stack)
        
        return realString(S) == realString(T)
