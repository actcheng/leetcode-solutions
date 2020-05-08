# Problem 1232 
# Date completed: 2019/10/30 

# 72 ms (80%)
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3: return True
        if coordinates[0][0]==coordinates[1][0]: # Vertical
            return all(coordinates[0][0] == coord[0] for coord in coordinates[1:])
        else:
            slope = (coordinates[0][1]-coordinates[1][1])/(coordinates[0][0]-coordinates[1][0])
            intercept = (coordinates[0][0]*coordinates[1][1]-coordinates[1][0]*coordinates[0][1])/(coordinates[0][0]-coordinates[1][0])
            return all((coordinates[0][1]-coord[1])/(coordinates[0][0]-coord[0]) == slope and (coordinates[0][0]*coord[1]-coord[0]*coordinates[0][1])/(coordinates[0][0]-coord[0]) == intercept for coord in coordinates[1:])

# 2020/05/08
# 64 ms
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2: return True
        x0 = coordinates[1][0]-coordinates[0][0]
        y0 = coordinates[1][1]-coordinates[0][1]
        return all(x0*(coord[1]-coordinates[0][1])==y0*(coord[0]-coordinates[0][0]) for coord in coordinates[2:])        
