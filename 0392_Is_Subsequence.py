# Problem 392 
# Date completed: 2019/09/18

# 44 ms
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        while s:
            try: 
                ind = t.index(s[0])
            except: 
                return False
            
            t = t[ind+1:]
            if len(s)>1: 
                s = s[1:]
            else:
                return True
            
            # print(t,s)
            
        return True
            
