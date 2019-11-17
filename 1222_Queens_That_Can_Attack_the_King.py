# Problem 1222
# Date completed: 2019/11/17 

# 36 ms (99%)
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        board = [['']*8 for i in range(8)]
        for queen in queens:
            board[queen[0]][queen[1]] = True
            
        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
        attack = []
        for i in range(8):
            dx, dy = directions[i]
            x,y = king
            while True:
                x += dx
                y += dy
                if x<0 or x>7 or y<0 or y>7:
                    break
                elif board[x][y]:
                    attack.append([x,y])
                    break

        return attack
