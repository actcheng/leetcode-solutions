# Problem 884 
# Date completed: 2019/09/13

# 36 ms
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        listA, listB  = A.split(), B.split()
        setAB = set(listA)^set(listB)        
        return [x for x in setAB if (listA.count(x)+listB.count(x)) == 1]
