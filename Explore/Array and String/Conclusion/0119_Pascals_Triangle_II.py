# Problem 119
# Date completed: 2019/09/29 

# 32 ms
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            row = [1]+[row[j]+row[j+1] for j in range(i)]+[1]           
        return row
        
# 52 ms
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        row = [1,1]
        for i in range(1,rowIndex):
            row = [1]+[row[j]+row[j+1] for j in range(len(row)-1)]+[1]           
        return row
