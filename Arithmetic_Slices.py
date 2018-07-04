# Problem #413
# Date completed: 2018/07/04
class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        alen=len(A)
        # Number of combinations from a slice with length n is
        # (n-2)+n*(n-3)-(n*(n-1)/2)+3
        
        i=0
        num=0
        while i<=alen-3:
            diff=A[i+1]-A[i]
            j=1
            quit=False
            while (i+j+1<len(A) and not quit):
                if A[i+j+1]==A[i]+diff*(j+1):
                    j+=1
                else:
                    quit=True
            if j>1:
                n=1+j
                num+=int((n-2)+n*(n-3)-(n*(n-1)/2)+3)
            i+=j
        
        return num
