# Problem 78
# Date completed: 2020/07/11 

# 28 ms (95%)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return [[]]        
        
        res = self.subsets(nums[1:])

        return res + [[nums[0]] + subset for subset in res]
