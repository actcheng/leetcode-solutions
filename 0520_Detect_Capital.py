# Problem 520
# Date completed: 2019/12/28 

# 20 ms (99%)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)<2: return True
        upper = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
        if word[0] in upper:
            if word[1] in upper:
                for i in range(2,len(word)):
                    if word[i] not in upper: return False
                return True
            else:
                for i in range(2,len(word)):
                    if word[i] in upper: return False
                return True
        else:
            for i in range(1,len(word)):
                if word[i] in upper: return False
            return True
        
