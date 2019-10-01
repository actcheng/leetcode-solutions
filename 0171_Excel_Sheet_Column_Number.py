# Problem 171
# Date completed: 2019/10/01

# 36 ms (84%)
class Solution:
    def titleToNumber(self, s: str) -> int:
        ref = {chr(i):i-ord('A')+1 for i in range(ord('A'),ord('Z')+1)}
        num = 0
        for x in s:
            num = num*26 + ref[x]
        return num
