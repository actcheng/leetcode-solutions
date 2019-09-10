 # Problem 905 
# Date completed: 2019/09/10

# 96 ms

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [a for a in A if a%2 ==0] + [a for a in A if a%2 ==1]
