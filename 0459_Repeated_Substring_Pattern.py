# Problem 459
# Date completed: 2019/09/26

# 148 ms
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s: return False
        substr = s[0]
        i = 1
        j = 1
        l = len(s)
        while i+len(substr) <= l:
            # print(substr,s[i:i+len(substr)])
            if s[i:i+len(substr)] != substr:
                i = j
                substr = s[:i+1]
                j +=1
                i +=1
                # print(i)
            else:
                i+= len(substr)
        # print(substr)
        return l//len(substr) > 1 and  l % len(substr) ==0
