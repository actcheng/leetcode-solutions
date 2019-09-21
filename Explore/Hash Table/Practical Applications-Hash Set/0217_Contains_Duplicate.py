# Problem 217 
# Date completed: 2019/09/21

# 136 ms
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
