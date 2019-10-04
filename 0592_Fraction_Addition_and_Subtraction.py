# Problem 592
# Date completed: 2019/10/04

# 48 ms (14%)
class Solution:
    def fractionAddition(self, expression: str) -> str:
        arr = [int(x) for x in expression.replace('+',' +').replace('-',' -').replace('/',' ').split()]
        if len(arr)%2 > 0: return
        num, den = 0, 1
        
        hist = []
        for i in range(len(arr)//2):
            if arr[2*i+1] not in hist:
                num = num*arr[2*i+1] + den*arr[2*i]
                den *= arr[2*i+1]
                hist.append(den)
            else:
                num += den//arr[2*i+1]*arr[2*i]
        
        if num == 0: return '0/1'
        
        i = 2
        while i <= abs(num) and i<=den:
            while num%i == den%i == 0:
                num = num // i
                den = den // i
            i +=1
                
        return f'{num}/{den}'
