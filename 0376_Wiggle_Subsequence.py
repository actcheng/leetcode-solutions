# Problem 376
# Date completed: 2019/12/22 

# 28 ms (96%)
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        res = 1
        extra = 0
        for i in range(len(nums)-1):
            if res == 1:                
                if nums[i] != nums[i+1]:
                    res += 1
                    if nums[i] > nums[i+1]:
                        res += 1
                        extra = -1
            else:
                if res % 2: 
                    if nums[i] < nums[i+1]:
                        res += 1
                else:
                    if nums[i] > nums[i+1]:
                        res += 1
                        
        return res+extra
