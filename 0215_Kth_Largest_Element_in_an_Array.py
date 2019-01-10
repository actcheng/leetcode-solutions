# Problem #215
# Date completed: 2019/01/11

# 68 ms
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
    
        return sorted(nums)[-k]
