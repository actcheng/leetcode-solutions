# Problem 594
# Date completed: 2020/01/19 

# 344 ms (57%)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        keys = sorted(counts.keys())
        res = 0
        for i in range(len(keys)-1):
            if keys[i+1]-1 == keys[i]:
                res = max(res,counts[keys[i+1]]+counts[keys[i]])
        return res
        
