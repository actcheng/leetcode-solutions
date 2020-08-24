# Problem 497
# Date completed: 2020/08/22

# 372 ms (7%)
class Solution:
    import random
    def __init__(self, rects: List[List[int]]):
        
        self.rects = rects
        self.weights = [(rect[2]-rect[0]+1)*(rect[3]-rect[1]+1) for rect in rects]
        
    def pick(self) -> List[int]:

        rect = random.choices(self.rects,self.weights)[0]
        return [randint(rect[0],rect[2]), randint(rect[1],rect[3])]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
