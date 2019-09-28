# Problem 54
# Date completed: 2019/09/28

# 40 ms
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return 
        h,w = len(matrix), len(matrix[0])        
        i,j = 0,-1
        incI, incJ = 0, 1
        minI, maxI = 0, h-1
        minJ, maxJ = 0, w-1
        ans = []
        while len(ans)<h*w:            
            i += incI
            j += incJ
            if i < minI:
                i = minI
                incI,incJ = 0,1
                minJ += 1
            elif i > maxI:
                i = maxI
                incI, incJ = 0,-1
                maxJ -= 1
            elif j < minJ:
                j = minJ
                incI, incJ = -1, 0
                maxI -=1
            elif j > maxJ:
                j = maxJ
                incI,incJ = 1, 0
                minI +=1
            else:
                ans.append(matrix[i][j])
        return ans
