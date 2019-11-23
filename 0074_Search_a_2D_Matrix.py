# Problem 74
# Date completed: 2019/11/23 

# 80 ms (51%)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]: return False
        h,w = len(matrix), len(matrix[0])
        # search row
        low, up = 0, h-1
        while low+1<up:
            mid = (up+low)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid
            else:
                up = mid
                
        row = up if matrix[up][0]<=target else low  
        
        left, right = 0, w-1
        while left+1 < right:
            mid = (left+right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid
            else:
                right = mid

        return matrix[row][left] == target or matrix[row][right] == target
