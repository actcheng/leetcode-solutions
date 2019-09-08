# Problem 20
# Date completed: 2019/09/08

# 40 ms
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(',']':'[','}':'{'}
        stack = []
        for bracket in s:
            if bracket in brackets.values(): stack.append(bracket)
            if bracket in brackets.keys():
                if not (stack and stack.pop() == brackets[bracket]): return False

        return stack == []

        
