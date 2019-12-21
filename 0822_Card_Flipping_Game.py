# Problem 822
# Date completed: 2019/12/22 

# 104 ms (94%)
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        both = set()
        one = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                both.add(fronts[i])
            else:
                one.add(fronts[i])
                one.add(backs[i])
                
        return min(one-both) if len(one-both)>0 else 0
