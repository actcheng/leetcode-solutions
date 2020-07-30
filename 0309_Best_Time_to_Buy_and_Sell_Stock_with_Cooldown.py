# Problem 309
# Date completed: 2020/07/29

# 36 ms (92%)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = len(prices)
        
        if l < 2:
            return 0
        elif l == 2:
            return max(0,prices[1]-prices[0])
        
        with_stock = [0 for i in range(l)]
        no_stock = [0 for i in range(l)]
        
        with_stock[0] = -prices[0]
        no_stock[0] = 0
        
        with_stock[1] = max(-prices[1],with_stock[0])
        no_stock[1] = max(with_stock[0]+prices[1],no_stock[0])
        
        for i in range(2,l):
            with_stock[i] = max(no_stock[i-2]-prices[i],with_stock[i-1])
            no_stock[i] = max(with_stock[i]+prices[i],no_stock[i-1])
            
        return no_stock[-1]
