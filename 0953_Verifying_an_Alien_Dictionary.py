# Problem 953
# Date completed: 2019/12/22 

# 40 ms (59%)
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        store = {order[i]:i for i in range(len(order))}
        
        def compareTwoWords(w1,w2): # check if w1 > w2
            for i in range(len(w1)):
                if i >= len(w2) or store[w1[i]] > store[w2[i]]: 
                    return False
                elif store[w1[i]] < store[w2[i]]:
                    return True
                
        for i in range(len(words)-1):
            if words[i] != words[i+1] and not compareTwoWords(words[i],words[i+1]): return False
            
        return True
