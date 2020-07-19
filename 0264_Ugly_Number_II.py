# Problem 264
# Date completed: 2020/07/04 

# 320 ms (34%)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        cur = 1
        factor = [2,3,5]
        li = [[f] for f in factor] # Use linked list?
        
        for i in range(n-1):
            cur = min(li[0][0],li[1][0],li[2][0])
            for j in range(3):
                if li[j][0] == cur: li[j].pop(0)
                li[j].append(cur*factor[j])
        
        return cur
