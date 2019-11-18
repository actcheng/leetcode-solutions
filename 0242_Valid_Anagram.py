# Problem 242
# Date completed: 2019/11/18 

# 36 ms (98%)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
