# Problem 387 
# Date completed: 2019/09/10

# 232 ms

class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = {}
        checked = []
        for i in range(len(s)):
            c = s[i]            
            if c in unique.keys():
                del unique[c]
            elif c not in checked:
                unique[c] = i
                checked.append(c)
            
        keys = list(unique.keys())
        
        if keys:
            return unique[keys[0]]
        else:
            return -1
