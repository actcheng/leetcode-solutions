# Problem 506
# Date completed: 2019/12/27 

# 68 ms (91%)
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        store = {nums[i]:i for i in range(len(nums))}
        keys = sorted(store.keys(),reverse=True)
        res = list(nums)
        for i in range(len(keys)):
            if i==0:
                place = 'Gold Medal'
            elif i==1:
                place = 'Silver Medal'
            elif i ==2:
                place = 'Bronze Medal'
            else:
                place = str(i+1)
            res[store[keys[i]]] = place
        return res
        
