# Problem 454
# Date completed: 2019/09/28 

# 380 ms
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if not (A and B and C and D): return 0
        from collections import Counter, defaultdict
        unique = [Counter(x) for x in [A,B,C,D]]
        comb1 = defaultdict(int)
        comb2 = defaultdict(int)
        for x in unique[0]:
            for y in unique[1]:
                comb1[x+y] += unique[0][x]*unique[1][y]
        for x in unique[2]:
            for y in unique[3]:
                comb2[-(x+y)] += unique[2][x]*unique[3][y]
        # print(len(comb1),len(comb2))

        keys = comb1.keys() & comb2.keys()
        
        return sum([comb1[key]*comb2[key] for key in keys])
