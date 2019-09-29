# Problem 26 
# Date completed: 2019/09/17

# 104 ms
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 
        n = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i] == n:
                nums.pop(i)
            else:
                n = nums[i]
        return len(nums)
            
