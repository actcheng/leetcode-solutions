# Problem 961
# Date completed: 2019/12/09 

# 212 ms (98%)
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        s = set()
        for a in A:
            if a in s: return a
            s.add(a)
