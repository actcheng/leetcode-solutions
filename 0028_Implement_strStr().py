# Problem 28
# Date completed: 2019/09/26 

# 40 ms
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '': return 0
        l = len(needle)
        for i in range(len(haystack)-l+1):
            if haystack[i:i+l] == needle: return i

        return -1
