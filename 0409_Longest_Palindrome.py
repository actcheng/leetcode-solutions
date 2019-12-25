# Problem 409
# Date completed: 2019/12/25 

# 28 ms (92%)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = collections.Counter(s)
        res = 0
        for key in list(counts.keys()):
            res += 2*(counts[key] // 2)
            counts[key] %= 2
            if counts[key] == 0: del counts[key]
            
        if len(counts) > 0: res += 1
        return res
