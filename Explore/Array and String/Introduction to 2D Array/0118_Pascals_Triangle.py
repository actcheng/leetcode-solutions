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

# 2019/09/28
# 36 ms
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        triangle = []
        for i in range(numRows):
            if i == 0:
                triangle.append([1])
            else:
                triangle.append([1]+[triangle[i-1][j]+triangle[i-1][j+1] for j in range(i-1) if i >0] + [1])
        return triangle
