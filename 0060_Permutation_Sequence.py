# Problem 60
# Date completed: 2020/06/21

# 28 ms, 83%

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        pool = [str(i) for i in range(1,n+1)]
        res = ''
        comb = 1
        for i in range(1,n):
            comb *= i

        for i in range(n-1,0,-1):
            j = (k-1) // comb
            k -= j*comb
            comb =  comb // i 
            res += pool[j]
            pool = pool[:j] + pool[j+1:]
            
        res += pool[-1]
        return res
            
