# Problem 36
# Date completed: 2019/09/24 

# 108 ms
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        row = defaultdict(list) 
        col = defaultdict(list) 
        box = defaultdict(list) 
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                    box[(i//3,j//3)].append(board[i][j])
        return all(len(row[i]) == len(set(row[i])) for i in row) and \
               all(len(col[i]) == len(set(col[i])) for i in col) and \
               all(len(box[i]) == len(set(box[i])) for i in box)
