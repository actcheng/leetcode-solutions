# Problem 525
# Date completed: 2020/04/14 

# 24 ms (%)

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        length = len(s)
        start = 0
        move = {0:1,1:-1}
        for direction, amount in shift:
            start = (start + amount*move[direction]) % length
        return s[start:]+s[:start]
