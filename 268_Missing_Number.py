# Problem 268
# Date completed: 2018/07/04

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        a = int(m*(m+1)/2)-sum(nums)
        return a
