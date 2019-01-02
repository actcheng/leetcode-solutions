# Problem 414
# Date completed: 2019/01/02

# 52 ms
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = max(nums)
        try:
            nums = list(filter((first).__ne__, nums))
            second = max(nums)
        except:
            return first
        
        try:
            nums = list(filter((second).__ne__, nums))
            third = max(nums)
        except:
            return first
        
        return third
            
        
