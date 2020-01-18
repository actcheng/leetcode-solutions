# Problem 1030
# Date completed: 2020/01/18 

# 272 ms (7%)
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        matrix = [[True]*C for col in range(C) for row in range(R)]
        matrix[r0][c0] = False
        queue = [[r0,c0]]
        res = [[r0,c0]]
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while queue:
            r,c = queue.pop(0)
            for dr,dc in directions:
                new_r, new_c = r+dr, c+dc
                if (0 <= new_r < R and 
                    0 <= new_c < C and
                    matrix[new_r][new_c]):
                    matrix[new_r][new_c] = False
                    queue.append([new_r,new_c])
                    res.append([new_r,new_c])
        return res

# One line
# 160 ms (89%)
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:    
        return sorted([(i,j) for i in range(R) for j in range(C)],key=lambda pos: abs(pos[0]-r0)+abs(pos[1]-c0))


