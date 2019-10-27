# Problem 383
# Date completed: 2019/10/27 

# 65 ms (68%)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ranCount = collections.Counter(ransomNote)
        magCount = collections.Counter(magazine)
        
        for letter in ranCount:
            if letter not in ranCount or magCount[letter] < ranCount[letter]:
                print
                return False
            
        return True
