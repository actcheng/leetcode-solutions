# Problem 290
# Date completed: 2019/09/23 

# 40 ms
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = str.split()
        if not pattern and not s: return False
        if len(pattern) != len(s): return False

        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if s[i] not in d.values():
                    d[pattern[i]] = s[i]
                else:
                    return False
            elif d[pattern[i]] != s[i]:
                return False
        return True
