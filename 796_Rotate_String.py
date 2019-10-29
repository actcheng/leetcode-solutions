# Problem 796 
# Date completed: 2019/10/29

# 32 ms (90%)
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A)==len(B) and A in B*2
