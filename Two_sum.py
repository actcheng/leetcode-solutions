# Problem #1
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if (nums[i]+nums[j]==target and i!=j):
                    return [i,j]
