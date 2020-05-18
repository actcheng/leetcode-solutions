# Problem 567
# Date completed: 2020/05/18 

# 68 ms (76%)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return []
        l = len(s1)
        counts_1 = collections.Counter(s1)
        counts_2 = collections.Counter(s2[:l])
        diff = {}
        n_diff = 0
        res = []
        for a in counts_1:
            diff[a] = counts_1[a] - counts_2[a]
            n_diff += abs(diff[a])
        
        if n_diff == 0: return True
        
        for i in range(1,len(s2)-l+1):
            if s2[i-1] == s2[i+l-1]: continue
            
            if s2[i-1] in diff:
                n_diff += 1 if diff[s2[i-1]] >= 0 else -1
                diff[s2[i-1]] += 1
                
            if s2[i+l-1] in diff:
                n_diff += 1 if diff[s2[i+l-1]] <= 0 else -1
                diff[s2[i+l-1]] -= 1
                
            if n_diff == 0: return True
        
        return False
