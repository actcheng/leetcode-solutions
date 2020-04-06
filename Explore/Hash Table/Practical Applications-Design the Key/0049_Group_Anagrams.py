# Problem 49
# Date completed: 2019/09/22 

# 116 ms
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = {}
        for s in strs:
            key = ''.join(sorted(list(s)))
            if key in hashTable:
                hashTable[key].append(s)
            else:
                hashTable[key] = [s]
        return list(hashTable.values())
    
# 2020/04/06
# 208 ms
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def sort(s):
            counts = collections.Counter(s)
            letters = sorted(list(counts.keys()))
            return ''.join([l*counts[l] for l in letters])
                           
        groups = collections.defaultdict(list)
        [groups[sort(s)].append(s) for s in strs]
        
        return list(groups.values())
    
# 192 ms
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def sort(s):
            counts = collections.Counter(s)
            letters = sorted(list(counts.keys()))
            return ''.join([l*counts[l] for l in letters])
                           
        groups = collections.defaultdict(list)
        [groups[sort(s)].append(s) for s in strs]
        
        return list(groups.values())
