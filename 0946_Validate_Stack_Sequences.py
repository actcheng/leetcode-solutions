# Problem 946
# Date completed: 2020/01/19 

# 80 ms (25%)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        arr = []
        for pp in popped:
            while (len(arr)==0 or arr[-1]!=pp) and pushed:
                arr.append(pushed.pop(0))
            if len(arr)==0 or arr[-1]!=pp: return False
            arr.pop()
        return True
                         
