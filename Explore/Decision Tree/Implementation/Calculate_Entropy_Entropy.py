# Calculate Entropy
# Date completed: 2019/10/13 

class Solution:
    def calculateEntropy(self, input: List[int]) -> float:
        if not input: return 0
        from math import log2
        counts = collections.Counter(input)
        n = len(input)
        entropy = sum([counts[x]*log2(counts[x]/n) for x in counts])/n
        return -entropy if entropy != 0 else 0
        
