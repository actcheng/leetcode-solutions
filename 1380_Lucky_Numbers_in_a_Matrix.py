# Problem 1380
# Date completed: 2020/08/24 

# 140 ms (75%)
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        h, w = len(matrix), len(matrix[0])
        row_min = set(min(row) for row in matrix)
        col_max = [matrix[0][i] for i in range(w)]
        
        for row in matrix:
            for i in range(w):
                if row[i] > col_max[i]: col_max[i] = row[i]
        
        return list(row_min & set(col_max))
