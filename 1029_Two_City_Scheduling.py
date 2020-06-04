# Problem 1029
# Date completed: 2020/06/04 

# 44 ms (50%)

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs,key=lambda x: x[1]-x[0],reverse=True)
        N = len(costs) // 2
        return sum(costs[i][0  if i < N else 1] for i in range(2*N))
