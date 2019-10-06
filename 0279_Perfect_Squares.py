# Problem 279
# Date completed: 2019/10/06 

# 2176 ms (20%)
class Solution:
    def numSquares(self, n: int) -> int:
        self.rec = {}
        
        def helper(m):
            if m<4: return m

            sq = int(m**(0.5))
            if sq*sq == m: return 1
            least = m
            for i in range(sq,1,-1):
                num = m-i*i
                if num not in self.rec :
                    self.rec[num] = helper(num)+1

                ans = self.rec[num]
                if ans == 2: return 2   
                if least > ans: least = ans

            return least
        
        return helper(n)

