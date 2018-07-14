# Solution 1 (296 ms)
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
    
        if x<0:
            return False
        
        r=0
        y=x
        while y>0:
            d=y%10
            r=r*10+d
            y=(y-d)/10
            
        return int(r)==x

# Solution 2 (428 ms)
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
    
        y=str(x)
        r=y[::-1]
        return y==r
