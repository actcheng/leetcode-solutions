# Problem 877
# Date completed: 2019/10/23 

# 952 ms (5%)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        self.scores = {}
        # Dynamic programming
        def helper(i,j):
            if i==j: return 0
            if (i,j) in self.scores: return self.scores[(i,j)]
            parity = 1 if (i+j) % 2 == 1 else -1
            if parity == 1: # Alex's turn
                self.scores[(i,j)] = max(piles[i]+helper(i+1,j),piles[j]+helper(i,j-1))
            else:
                self.scores[(i,j)] = min(-piles[i]+helper(i+1,j),-piles[j]+helper(i,j-1))
            
            return self.scores[(i,j)]
        
        return helper(0,len(piles)-1) > 0
