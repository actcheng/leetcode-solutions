# Problem 1122
# Date completed: 2020/03/01 

# 32 ms (86%)

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        tail = []
        res = []
        counts = {y:0 for y in arr2}
        
        for x in arr1:
            if x in counts:
                counts[x] += 1
            else:
                tail.append(x)
                
        for y in arr2:
            res.extend([y]*counts[y])
            
        return res + sorted(tail)
