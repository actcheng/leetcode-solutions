# Problem 79
# Date completed: 2019/11/18 

# 420 ms (31%)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if not word or not board or not board[0]: return False
        # [print(row) for row in board]
        self.h,self.w = len(board), len(board[0])
        self.l = len(word)
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def searchWord(loc,k,checked):
            checked[loc[0]][loc[1]] = True
            if k == self.l:
                return True
            else:
                for direction in directions:
                    x = loc[0]+direction[0]
                    y = loc[1]+direction[1]
                    if (x>=0 and x<self.h and 
                        y>=0 and y<self.w and 
                        not checked[x][y] and 
                        board[x][y]==word[k]):
                        if searchWord([x,y],k+1,checked): return True
                checked[loc[0]][loc[1]] = False
                return False
        
        for i in range(self.h):
            for j in range(self.w):
                if board[i][j]==word[0]:
                    checked = [[False]*self.w for k in range(self.h)]
                    if searchWord([i,j],1,checked): return True
        return False        
