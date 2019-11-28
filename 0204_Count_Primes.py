# Problem 204
# Date completed: 2019/11/28 

# 844 ms (38%)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3: return 0
        isPrime = [True for i in range(n)]
        isPrime[:2] = [False, False] 
        
        maxI = int(n**(0.5))
        for i in range(2,maxI+1):
            if isPrime[i]:
                maxJ = n//i
                for j in range(i,maxJ+1):
                    if j*i<n: isPrime[j*i] = False

#         print([i for i in range(n) if isPrime[i]])
        return sum(isPrime)
