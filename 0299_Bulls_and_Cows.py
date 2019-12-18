# Problem 299
# Date completed: 2019/12/19 

# 36 ms (91%)
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        counts_secret, counts_guess = {}, {}        
        
        for s, g in zip(secret,guess):
            if s == g: 
                bulls += 1
            else:
                if s in counts_secret:
                    counts_secret[s] += 1
                else:
                    counts_secret[s] = 1
                    
                if g in counts_guess:
                    counts_guess[g] += 1
                else:
                    counts_guess[g] = 1
    
        for s in counts_secret:
            if s in counts_guess:
                cows += min(counts_secret[s],counts_guess[s])

        return f'{bulls}A{cows}B'
                    
