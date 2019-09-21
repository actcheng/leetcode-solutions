# Problem 219
# Date completed: 2019/09/21

# 112 ms
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or k == 0: return False
        nearby = set()
        
        for i in range(min(len(nums),k+1)):
            if nums[i] in nearby:
                return True
            else:
                nearby.add(nums[i])
                
        if len(nums) <= k: return False
        
        for i in range(len(nums)-k-1):
            nearby.remove(nums[i])
            if nums[i+k+1] in nearby:
                return True
            else:
                nearby.add(nums[i+k+1])            
            
        return False
        
# Sample solution: 92 ms
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        
        for i,num in enumerate(nums):
            if num in dic:
                if i - dic[num] <= k:
                    return True
            dic[num] = i
                
        return False
