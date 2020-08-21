# Problem 967
# Date completed: 2020/08/18

# 44 ms (62%)
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1: return [i for i in range(10)]
        if K == 0: return [''.join([str(i)]*N) for i in range(1,10)]
        
        res = []
        
        def dfs(arr,prev):
            if len(arr) == N:
                res.append(''.join(arr))
            else:
                for d in [prev-K,prev+K]:
                    if 0<=d <= 9:
                        dfs(arr+[str(d)],d)
        
        for i in range(1,10): 
            dfs([str(i)],i)
            
        return res
