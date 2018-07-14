# Problem 118
# Complete date: 2018/07/14

# 36 ms
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        from math import factorial
        l=[]
        for i in range(numRows):
            temp=[1]*(i+1)
            if i>1:
                for j in range(1,i):
                    temp[j]=l[i-1][j-1]+l[i-1][j]
            l.append(temp)            
            
        return l
