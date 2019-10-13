# Problem 657
# Date completed: 2019/10/13 

# 160 ms (5%)
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        directions = {'U':[0,1] ,'D': [0,-1], 'R': [1,0],'L':[-1,0]}
        loc = [0,0]
        for move in list(moves):
            for i in range(2):
                loc[i] += directions[move][i]
                
        return loc[0]==loc[1]==0
        
       
# Much faster way: Just compare the counts of 'U' vs 'D', 'R' vs 'L'!!!
