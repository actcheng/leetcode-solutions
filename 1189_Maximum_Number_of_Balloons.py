# Problem 1189
# Date completed: 2019/09/15

# 52 ms
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {'b':1,'a':1,'l':2,'o':2,'n':1}
        return min([text.count(x)//letters[x] for x in letters])
        
