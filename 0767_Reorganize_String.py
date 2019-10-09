# Problem 767
# Date completed: 2019/10/09 

# 40 ms (64%)
class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        counts = collections.OrderedDict(collections.Counter(list(S)).most_common()[::-1])
        
        if max(list(counts.values())) > (n+1)/2: return ""
        keys = list(counts.keys())
        A = []
        for key in keys:
            A.extend(key*counts[key])
        A[::2],A[1::2] = A[n//2:], A[:n//2]
        return ''.join(A)
