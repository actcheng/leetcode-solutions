# Problem 1051
# Date completed: 2019/11/20 

# 32 ms (96%)
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort = sorted(heights)
        return sum([sort[i]!=heights[i] for i in range(len(heights))])
