# Problem 942 
# Date completed: 2019/09/02

# 88 ms
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        top = len(S)
        bottom = 0
        ans = []
        for s in S:
            if s == 'I':
                ans.append(bottom)
                bottom += 1
            else:
                ans.append(top)
                top -= 1
                
        ans.append(top)
        
        return ans
