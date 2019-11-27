# Problem 791
# Date completed: 2019/11/27 

# 28 ms (93%)

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        counts = collections.Counter(T)
        res = ''
        for char in S:
            if char in counts:
                res += counts[char]*char
                del counts[char]
                
        for char in counts:
            res += counts[char]*char
            
        return res

