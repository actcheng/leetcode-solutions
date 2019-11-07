# Problem 779
# Date completed: 2019/11/07

# 20 ms (100%)
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1: 
            return '0'
        elif N == 2:
            return '0' if K==1 else '1'
        else:
            ind = 2**(N-3)
            if K <= ind*2: 
                prevK = K
            elif K<=ind*3:
                prevK = K-ind
            else:
                prevK = K-ind*3
            # print('prevK',prevK)
            return self.kthGrammar(N-1,prevK)
        
# Shorter
# 28 ms (98%)
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N <= 2:
            return '0' if K==1 else '1'
        else:
            ind = 2**(N-3)
            prevK = K if K <= ind*2 else K-ind if K<=ind*3 else K-ind*3
            return self.kthGrammar(N-1,prevK)
