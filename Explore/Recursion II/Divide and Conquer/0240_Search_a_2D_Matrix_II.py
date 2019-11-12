# Problem 240
# Date completed: 2019/11/12 

# 28 ms (99%)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        
        def binary_search(col):
            # Binary search: find row that is just larger than target
            l, r = 0, len(matrix)-1
            while l+1<r:
                row = (l+r)//2
                mid = matrix[row][col]
                if mid== target:
                    return row
                elif mid < target:
                    l = row
                else:
                    r = row
            return l if matrix[l][col] >= target else r
        
        h, w = len(matrix), len(matrix[0])
        if h == w == 1: 
            return matrix[0][0] == target
        col = w//2       
        row = binary_search(col)
        
        return matrix[row][col] == target \
               or self.searchMatrix([r[col+1:] for r in matrix[:row+1]], target) \
               or self.searchMatrix([r[:col] for r in matrix[row:]], target) 
