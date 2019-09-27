# Problem 747
# Date completed: 2019/09/27 

# 44 ms
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        ind = nums.index(largest)
        return -1 if any([largest/x <2 and x != largest for x in nums if x>0]) else ind
