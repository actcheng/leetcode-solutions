# Problem 14
# Date completed: 2019/09/25

# 40 ms
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        if len(strs) == 1: return strs[0]
        prefix = ''
        l = min(len(s) for s in strs)
        n = len(strs)
        for i in range(l):
            letter = strs[0][i]
            if all(strs[j][i]==letter for j in range(1,n)):
                prefix += letter
            else:
                break
        
        return prefix
