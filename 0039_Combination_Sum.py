# Problem 39
# Date completed: 2019/10/12 

# 72 ms (66%)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or target < min(candidates): return []

        arrs = []
        for i,x in enumerate(candidates):
            if target == x: 
                arrs.append([target])
            else: 
                arr = self.combinationSum(candidates[i:],target-x)
                if arr: 
                    for a in arr:
                        arrs.append([x]+a)

        return arrs
