# Problem 504
# Date completed: 2020/01/14 

# 28 ms (61%)
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        sign = -1 if num < 0 else 1
        num = abs(num)
        places = 1
        accum = 7
        while num >= accum:
            accum *= 7
            places += 1
            
        accum /= 7
        res = ''
        for i in range(places):
            res += str(int(num//accum))
            num %= accum
            accum /= 7
            
        return res if sign==1 else '-'+res
        
