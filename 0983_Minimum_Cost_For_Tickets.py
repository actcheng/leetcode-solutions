
# Problem 983
# Date completed: 2020/08/25 

# 72 ms (24 ms)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        memo = {}
        
        def dp(day):
            if day <= 0: 
                return 0
            elif day not in memo: 
                memo[day] = dp(day-1)

            return memo[day]

        for day in days:
            memo[day] = min([dp(day-1)+costs[0], dp(day-7)+costs[1],dp(day-30)+costs[2]])
 
        return memo[days[-1]]
            
