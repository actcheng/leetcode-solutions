# Problem 405
# Date completed: 2020/01/15 

# 28 ms (57%)
class Solution:
    def toHex(self, num: int) -> str:
        if 0 <= num < 10: return str(int(num))
        if num < 0: num += 2**32
            
        lib = list('0123456789abcdef')
        places = 0
        accum = 1
        while num >= accum:
            accum *= 16
            places += 1
            
        accum /=16
        res = ''
        for i in range(places):
            res += lib[int(num//accum)]
            places -= 1
            num %= accum
            accum /= 16
            
        return res
