# Problem 1078
# Date completed: 2019/12/01 

# 28 ms (89%)
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        if len(words) < 3: return []
        
        matchFirst = False
        res = []
        
        for i,word in enumerate(words[:-1]):
            if matchFirst:
                if word == second: res.append(words[i+1])
                matchFirst = False
            matchFirst = (word==first) 
                    
        return res
