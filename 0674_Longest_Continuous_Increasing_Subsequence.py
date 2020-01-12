# Problem 674
# Date completed: 2020/01/12 

# 80 ms (55%)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        length = 1
        res = 1
        
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                length += 1
            elif length > 1:
                res = max(res,length)
                length = 1
        
        return max(res,length) 
            
