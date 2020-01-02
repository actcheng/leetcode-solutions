# Problem 680
# Date completed: 2020/01/02 

# 172 ms (50%)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s: return True
        deleted = False
        i,j = 0,len(s)-1
        store = None
        while i<j:
            if s[i] != s[j]:
                if not deleted and (s[i] == s[j-1] or s[i+1] == s[j]) : 
                    if s[i] == s[j-1]:
                        if s[i+1] == s[j]: store=(i+1,j)
                        j-=1
                    elif s[i+1] == s[j]:
                        i+=1
                    deleted=True
                else: 
                    if store:
                        i,j = store
                        store = None
                    else:
                        return False
            i+=1
            j-=1
            
        return True
