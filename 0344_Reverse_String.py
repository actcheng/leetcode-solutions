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
        
