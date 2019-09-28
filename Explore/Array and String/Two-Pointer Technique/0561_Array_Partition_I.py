# Problem 561
# Date completed: 2019/09/28

# 352 ms
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return sum([nums[2*i] for i in range(len(nums)//2)])
