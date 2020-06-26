# Problem 130
# Date completed: 2020/06/18 

# 144 ms, 73 %

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        
        h, w = len(board), len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        stack = [(0,j) for j in range(w) if board[0][j] == 'O'] + \
                [(h-1,j) for j in range(w) if board[h-1][j] == 'O'] + \
                [(i,0) for i in range(1,h-1) if board[i][0] == 'O' ] + \
                [(i,w-1) for i in range(1,h-1) if board[i][w-1] == 'O']

        while stack:
            y, x = stack.pop()
            if board[y][x] == 'O':
                board[y][x] = '_'
                for dy, dx in directions:
                    y_new, x_new = y+dy, x+dx
                    if 0<=y_new<h and 0<=x_new<w and board[y_new][x_new]=='O':
                        stack.append((y_new,x_new))
        
        d = {'X':'X','O':'X','_':'O'}
        for i in range(h):
            for j in range(w):
                board[i][j] = d[board[i][j]]
