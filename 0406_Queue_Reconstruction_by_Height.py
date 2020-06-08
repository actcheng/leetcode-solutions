# Problem 406
# Date completed: 2020/06/06

# 184 ms (30%)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        pos = collections.defaultdict(list)
        
        for h, k in people:
            pos[h].append(k)
            
        res = [[] for i in range(len(people))]
        keys = sorted(pos.keys())
        locs = [i for i in range(len(people))]
        c = 0
        for h in keys:
            queue = sorted(pos[h])
            c = 0
            for k in queue:
                res[locs[k-c]] = [h,k]
                locs = locs[:k-c] + locs[k-c+1:]
                c += 1
            # print(h,queue,locs)
            # print(res)
            
            
        return res
        
