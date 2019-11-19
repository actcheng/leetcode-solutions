# Problem 478
# Date completed: 2019/11/19 

# 156 ms (90%)
from math import cos, sin, pi, sqrt
from random import random

class Solution:  
    
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        l = self.radius*sqrt(random())
        ang = 2*pi*random()
        return [l*cos(ang) + self.x_center,
                l*sin(ang) + self.y_center]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
