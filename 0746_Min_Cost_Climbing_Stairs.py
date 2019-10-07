# Problem 746
# Date completed: 2019/10/07

# 64 ms (87%)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 2: return min(cost)
        total = [0]*n
        total[-1] = cost[-1]
        total[-2] = cost[-2]
        
        for i in range(n-3,-1,-1):
            total[i] = cost[i] + min(total[i+1], total[i+2])
            
        
        return min(total[0],total[1])
        
