# Problem 48
# Date completed: 2019/10/09 

# 48 ms (12%)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i,n-i-1):
                loc = [i,j] 
                temp1 = matrix[loc[0]][loc[1]]
                for k in range(5):                      
                    loc = [loc[1],n-loc[0]-1]
                    temp2 = matrix[loc[0]][loc[1]]
                    matrix[loc[0]][loc[1]] = temp1
                    temp1 = temp2
