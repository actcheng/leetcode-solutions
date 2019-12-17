# Problem 997
# Date completed: 2019/12/18 

# 788 ms (89%)
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        judge = []
        by = set([t[0] for t in trust])
        to = [t[1] for t in trust]
        for i in range(1,N+1):
            if i not in by and to.count(i) == N-1: return i            
        return -1

# 1292 ms (5%)
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        not_trust_by = {i:set(range(1,N+1))^{i} for i in range(1,N+1)}
        no_trust = set(range(1,N+1))
        for [b,t] in trust:
            if b in no_trust: no_trust.remove(b)
            if b in not_trust_by[t]: not_trust_by[t].remove(b)
        
        judge = []
        for p in no_trust:
            if len(not_trust_by[p])==0: judge.append(p)
        
        return judge[0] if len(judge) == 1 else -1

