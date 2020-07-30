# Problem 140
# Date completed: 2020/07/30 

# 84 ms (21%)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        l = len(s)
        wordDict = set(wordDict)
        dp = [[] for i in range(l+1)]
        dp[0] = ['']
        for i in range(1,l+1):
            for j in range(i-1,-1,-1):
                if len(dp[j]) > 0 and s[j:i] in wordDict:
                    dp[i].append(j)

        # print(dp)
        if len(dp[l]) == 0: return []
        
        def helper(ind):
            res = []
            for i in dp[ind]:
                if i == 0:
                    res.append(s[i:ind])
                elif len(dp[i]) > 0:
                    words = helper(i)
                    for word in words:
                        res.append(word+' ' +s[i:ind])
            return res
        return helper(l)
