# Problem 748 
# Date completed: 2019/09/18

# 76 ms
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        target = {}
        for s in licensePlate:
            if s.isalpha():
                if s.lower() in target:
                    target[s.lower()] += 1
                else:
                    target[s.lower()] = 1
        # print(target)
        
        matches = [word for word in words if not [a for a in target if word.count(a) < target[a]]]
        if not matches: return
        
        lens = [len(word) for word in matches]
        # print(matches, lens)
        return matches[lens.index(min(lens))]
