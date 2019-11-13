# Problem 686
# Date completed: 2019/11/14 

# 28 ms (99.7%)
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        setA, setB = set(A), set(B)
        if len(setB-setA)>0: return -1
        count = 1 if len(setA-setB)>0 else len(B) // len(A)
        print(count)
        for i in range(count,count+3):
            if B in A*i:
                return i
        return -1
        
