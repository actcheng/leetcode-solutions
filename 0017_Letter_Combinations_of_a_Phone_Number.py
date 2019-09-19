# Problem 17 
# Date completed: 2019/09/19

# 36 ms
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return
        
        letters={2:['a','b','c'],
                 3:['d','e','f'],
                 4:['g','h','i'],
                 5:['j','k','l'],
                 6:['m','n','o'],
                 7:['p','q','r','s'],
                 8:['t','u','v'],
                 9:['w','x','y','z']}
        
        res = letters[int(digits[0])]

        for d in digits[1:]:
            res = [r+l for r in res for l in letters[int(d)]]
            # print(res)
            
        return res
