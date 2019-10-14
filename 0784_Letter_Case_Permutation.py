# Problem 784
# Date completed: 2019/10/14 

# 68 ms (59%)
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        for i in range(len(S)):
            if S[i].isalpha():
                res = self.letterCasePermutation(S[i+1:])
                return [S[:i]+S[i].lower()+ r for r in res] + [S[:i]+S[i].upper()+ r for r in res]
        return [S]
