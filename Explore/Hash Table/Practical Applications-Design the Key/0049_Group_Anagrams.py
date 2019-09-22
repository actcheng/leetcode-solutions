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
