# Problem 451
# Date completed: 2020/05/22 

# 60 ms (33%)

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        freq = collections.defaultdict(list)
        for key in counts:
            freq[counts[key]].append(key)
            
        keys = sorted(freq.keys(),reverse=True)
        return ''.join([letter for key in keys for letter in freq[key] for i in range(key)])
        
        
