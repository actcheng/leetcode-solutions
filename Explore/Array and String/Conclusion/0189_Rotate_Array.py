# Problem 189
# Date completed: 2019/09/29 

# 72 ms
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-(k%len(nums)):]+nums[:-(k%len(nums))]
