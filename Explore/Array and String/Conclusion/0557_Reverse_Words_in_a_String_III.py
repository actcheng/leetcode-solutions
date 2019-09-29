# Problem 557 
# Date completed: 2019/09/20

# 36 ms
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([a[::-1] for a in s.split()])
