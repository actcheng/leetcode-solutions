# Problem 283
# Date completed: 2019/09/29

# 64 ms
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0 # Slow runner, locate next position for non zero
        for i in range(len(nums)): # Fast runner
            if nums[i] != 0:
                nums[j] = nums[i]
                if i>j: nums[i] = 0
                j += 1

        return nums
