# Problem 120
# Date completed: 2020/08/25 

# 56 ms (94%)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)

        for i in range(1,h):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[-1])
                
                
