# Problem 1047
# Date completed: 2019/10/14 

# 108 ms (30%)
class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        while i < len(S)-1:
            if S[i]==S[i+1]:
                S = S[:i]+S[i+2:]
                i = max(0,i-1)
            else:
                i += 1
        return S
