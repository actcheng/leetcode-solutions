# Problem 112
# Date completed: 2019/09/02

# 76 ms
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
        return sum(d for d in diff if d > 0)
