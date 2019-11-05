# Problem 344 
# Date completed: 2019/09/20

# 240 ms
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[-(i+1)]
            s[-(i+1)] = temp
        
# Date completed: 2019/11/05
# Recusive

# 260 ms
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left,right):
            s[left], s[right] = s[right],s[left]
            if left+1 < right-1: helper(left+1,right-1)        
        if not s: return 
        helper(0,len(s)-1)
