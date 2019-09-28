# Problem 67
# Date completed: 2019/09/28 

# 52 ms
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a: a="0"
        if not b: b="0"
        return str(bin(int(a,2)+int(b,2)))[2:]
