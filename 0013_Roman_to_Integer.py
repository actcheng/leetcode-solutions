# Problem 121
# Date completed: 2019/09/07

# 48 ms
class Solution:
    def romanToInt(self, s: str) -> int:
        if not s: return 0
        
        nums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        prev = nums[s[0]]
        for c in s:
            num = nums[c]
            ans += num 
            if num > prev: ans -= 2*prev 
            prev = num
        return ans
        
