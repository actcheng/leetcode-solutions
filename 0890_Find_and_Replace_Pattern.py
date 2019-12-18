# Problem 890
# Date completed: 2019/12/18 

# 32 ms (82%)
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        l = len(pattern)
        for word in words:
            if len(word) != l: continue
            px = {}
            x = set()
            match = True
            for i in range(l):
                if pattern[i] in px:
                    if px[pattern[i]] != word[i]: 
                        match = False
                        break
                else:
                    if word[i] in x:
                        match = False
                        break
                    else:
                        px[pattern[i]] = word[i]
                        x.add(word[i])
            if match: res.append(word)
        return res
