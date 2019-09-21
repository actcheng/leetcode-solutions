# Problem 205
# Date completed: 2019/09/21

# 36 ms
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replaced = {}
        new = ''
        for i in range(len(s)):
            if s[i] not in replaced:
                if t[i] in set(replaced.values()):
                    return False
                replaced[s[i]] = t[i]
            new += replaced[s[i]]
        return t == new
