# Problem 139
# Date completed: 2020/07/30 

# 32 ms (95%)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        l = len(s)
        dp = [False for i in range(l+1)]       
        dp[0] = True
        for i in range(l+1):
            for j in range(i-1,-1,-1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]  
