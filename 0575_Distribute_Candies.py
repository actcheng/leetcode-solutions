# Problem 575
# Date completed: 2019/12/24

# 856 ms (99%)
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(candies) // 2,len(set(candies)))
