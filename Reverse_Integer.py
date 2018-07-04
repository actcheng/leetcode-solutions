# Problem #7
# Date completed: 2018/07/04

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign=1
        y = str(x)[::-1]
        if y[-1]=="-":
            sign=-1
            y=y[:-1]
        i=0
        while(y[i]==0):
            y=y[1:]
            i+=1        
        
        ans=int(y)*sign
        if ans>(2**31-1) or ans<(-(2**31)):
            ans=0
        return ans
