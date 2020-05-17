# Problem 438
# Date completed: 2020/05/18 

# 156 ms (48%)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not p: return
        if len(p) > len(s): return []
        
        l = len(p)
        counts_p = collections.Counter(p)
        counts_s = collections.Counter(s[:l])
        diff = {}
        n_diff = 0
        res = []
        for a in counts_p:
            diff[a] = counts_p[a] - counts_s[a]
            n_diff += abs(diff[a])
        
        if n_diff == 0: res.append(0)

        for i in range(1,len(s)-l+1):
            if s[i-1] == s[i+l-1]: 
                if n_diff == 0: res.append(i)
                continue
            
            if s[i-1] in diff:
                n_diff += 1 if diff[s[i-1]] >= 0 else -1
                diff[s[i-1]] += 1
                
            if s[i+l-1] in diff:
                n_diff += 1 if diff[s[i+l-1]] <= 0 else -1
                diff[s[i+l-1]] -= 1

            if n_diff == 0: res.append(i)
        
        return res
