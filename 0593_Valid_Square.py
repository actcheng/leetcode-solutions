# Problem 593
# Date completed: 2019/09/23 


# 64 ms
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if not (p1 and p2 and p3 and p4): return False
        
        p = [p1,p2,p3,p4]
        d = []
        pair = []
        s4 = []
        for i in range(4):
            for j in range(i+1,4):
                d.append((p[i][0]-p[j][0])**2+(p[i][1]-p[j][1])**2)
                pair.append([i,j])
        l = [x for x in set(d) if d.count(x) ==4]
        if not l: return False
        
        for k in range(6):
            if d[k] == l[0]:
                i,j = pair[k]
                if p[i][1] - p[j][1] == 0: 
                    s4.append('undef')
                else:
                    s4.append((p[i][0]-p[j][0])/(p[i][1]-p[j][1]))  
        s2 = [s for s in set(s4) if s4.count(s) == 2]
        
        if len(s2) != 2: return False
        if 'undef' in s2: return 0 in s2
        return s2[0]*s2[1] +1 < 1e-8
