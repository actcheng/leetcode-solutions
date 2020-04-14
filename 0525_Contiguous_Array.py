# Problem 525
# Date completed: 2020/04/14 

# 892 ms (%)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        
        length = 0
        counts = {}
        count = 0
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count == 0:
                length = i+1
            elif count in counts:                 
                length = max(length,i-counts[count])
            else: 
                counts[count] = i
                
        return length
