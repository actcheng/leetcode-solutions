# Problem 1005
# Date completed: 2019/09/02

# 148 ms
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        ind = [i for i in range(len(seats)) if seats[i] == 1]
        diff = [ind[i+1] - ind[i] for i in range(len(ind)-1)]
        front, end = ind[0], 0
        
        if seats[-1] == 0:
            end = len(seats) - (ind[-1]+1)

        try: 
            return max([front, end, max(diff)//2])
        except:
            return max([front,end])
          
