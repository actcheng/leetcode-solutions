# Problem Calculate Maximum Information Gain
# Date completed: 2019/10/13 

class Solution:
    def calculateEntropy(self, counts,n):
        from math import log2
        if n==0: return 0    
        entropy = sum([counts[x]*log2(counts[x]/n) for x in counts if counts[x]>0])/n
        return -entropy if entropy != 0 else 0

    def calculateMaxInfoGain(self, petal_length: List[float], species: List[str]) -> float:
        if not petal_length: return 0
        
        counts2 = collections.Counter(species)
        n = len(species)
        entropy_orig = self.calculateEntropy(counts2,n)
        
        petal_length, species = zip(*sorted(zip(petal_length, species )))
        counts1 = collections.defaultdict(int)
        i = 0
        gain = []
        while i < n:
            counts1[species[i]] +=1
            counts2[species[i]] -=1
            
            while i < n-1 and petal_length[i] == petal_length[i+1]:
                i += 1
                counts1[species[i]] +=1
                counts2[species[i]] -=1
                
            # print(i,counts1, counts2)
            i += 1
            gain.append(entropy_orig-self.calculateEntropy(counts1,i)*i/n-self.calculateEntropy(counts2,n-i)*(n-i)/n)
        return max(gain)
