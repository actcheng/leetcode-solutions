# Problem 75
# Date completed: 2020/06/11

# 36 ms, 52%
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        while l < len(nums)-1 and nums[l] == 0: l+=1
        while r > 0 and nums[r] == 2: r -= 1 
        if l >= r: return
        i = l
        while i<=r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                while l < len(nums)-1 and nums[l] == 0: l+=1
                if l > i: i = l
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                while r > 0 and nums[r] == 2: r -= 1    
            else:
                i += 1
