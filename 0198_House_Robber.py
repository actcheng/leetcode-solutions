# Problem 198
# Date completed: 2019/11/30 

# 32 ms (83%)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) < 3: return max(nums)
        
        store = list(nums)
        store[2] += store[0]
        for i in range(3,len(store)):
            store[i] += max(store[i-2],store[i-3])
        
        return max(store[-1],store[-2])
