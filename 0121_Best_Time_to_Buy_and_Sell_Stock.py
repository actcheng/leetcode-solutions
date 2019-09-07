# Problem 121
# Date completed: 2019/09/07

# 76 ms

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        maxPro = 0
        minPrice = max(prices)
        for price in prices:
            if price < minPrice:
                minPrice = price                
            else:
                maxPro = max(maxPro, price - minPrice)

        return maxPro
