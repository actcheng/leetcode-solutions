# Problem 165
# Date completed: 2020/08/21 

# 40 ms (31%)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vers1 = version1.split('.')
        vers2 = version2.split('.')
        l = max(len(vers1),len(vers2))
        for i in range(l):
            v1 = int(vers1[i]) if i < len(vers1) else 0
            v2 = int(vers2[i]) if i < len(vers2) else 0
            
            if v1 > v2: 
                return 1
            elif v1 < v2:
                return -1
            
        return 0
