# Problem 738 
# Date completed: 2019/09/20

# 52 ms
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N < 10: return N
        
        digits = [int(n) for n in str(N)]
        res = 0
        l = len(digits)
        for i in range(l-1):
            if digits[l-i-1] < digits[l-i-2]:
                digits[l-i-1:] = [9]*(i+1)
                digits[l-i-2] -= 1
            
        for d in digits:
            res = res*10 + d

        return res
