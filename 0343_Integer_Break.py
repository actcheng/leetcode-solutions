# Problem 343
# Date completed: 2019/12/04 

# 36 ms (71%)
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 3: return 1
        store = [1,1] + [None]*(n-2)
        for i in range(2,n):
            store[i] = max([j*max(i-j+1,store[i-j]) for j in range(1,i)])
        return store[-1]
