# Problem 5
# Date completed: 2019/12/18 

# 1400 ms (52%)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        self.longest = s[0]
        l = len(s)               
                
        def expand(left,right):
            while left>=0 and right<l and s[left]==s[right]:
                res = s[left:right+1]
                left -= 1
                right += 1
            if len(res) > len(self.longest): self.longest=res
            return 
        
        for i in range(l-1):
            left,right = i,i+1
            if s[left]==s[right]: expand(left,right)
            if left>0 and s[left-1]==s[right]: expand(left-1,right)         
                
        return self.longest
