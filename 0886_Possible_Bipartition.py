# Problem 886
# Date completed: 2020/05/27 

# 1084 ms (18%)
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        rec = collections.defaultdict(set)
        for a,b in dislikes:            
            rec[a].add(b)
            rec[b].add(a)
        
        wait = set(rec.keys())
        queue = []
        groups = [set([]), set([])]
        group_dislike = [set([]),set([])]
        
        while queue or wait:
            key = queue.pop(0) if queue else wait.pop()
                
            for i in [0,1]:
                if key not in group_dislike[i]:
                    groups[i].add(key)
                    group_dislike[i].update(rec[key])
                    if key in wait: wait.remove(key)

                    for b in rec[key].intersection(wait):
                        if b in group_dislike[1-i]: 
                            print(b,groups)
                            return False
                        groups[1-i].add(b)
                        group_dislike[1-i].update(rec[b])
                        queue.extend([val for val in rec[b] if val in wait])
                        wait.remove(b)
                    break

            if len(group_dislike[0].intersection(group_dislike[1])) > 0: return False
        
        return True
