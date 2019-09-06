# Problem 581 
# Date completed: 2019/09/06

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        start, end = 0, 0

        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start = i
                break
                
        for i in range(len(nums)-start):
            if nums[-i-1] != sorted_nums[-i-1]:
                end = len(nums)-i
                break 

        return end - start
