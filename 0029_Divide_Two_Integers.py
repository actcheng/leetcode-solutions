# Problem 29
# Date completed: 2019/11/09 

# 24 ms (99%)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0: return 0
        sign = 1 if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        
        store = [divisor]
        while dividend > store[-1]:
            store.append(store[-1]+store[-1])
            
        quotient = 0    
        while store:
            if dividend >= store[-1]:
                quotient += 1<< (len(store)-1)
                dividend -= store[-1]
            else:
                store.pop()
                
        return  min(2**31-1, quotient) if sign == 1 else -min(2**31,quotient)
