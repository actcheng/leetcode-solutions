# Problem 986
# Date completed: 2020/05/23 

# 148 ms (96%)

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        pop_a, pop_b = True, True
        res = []
        while A or B:                    
            if pop_a: 
                if A:
                    start_a, end_a = A.pop(0)
                    pop_a = False
                else:
                    break
            if pop_b: 
                if B:
                    start_b, end_b = B.pop(0)
                    pop_b = False
                else:
                    break
            
            # Determine start          
            if start_b > end_a:
                pop_a = True
                continue
            elif start_a > end_b:
                pop_b = True
                continue            
            
            start = max(start_a,start_b)
            end   = min(end_a,end_b)
            if end_a == end_b:                
                pop_a, pop_b = True, True
            elif end_a < end_b:
                start_b = end_a
                pop_a = True
            else:
                start_a = end_b
                pop_b = True
                
            res.append([start,end])
            # print([start,end],[start_a,end_a],pop_a,[start_b,end_b],pop_b,len(A),len(B))
            
        return res
