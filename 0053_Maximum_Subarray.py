# Problem 53
# Date completed: 2019/12/18 

# 68 ms (83%)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return -2147483648
        m = nums[0]
        prev = nums[0]
        for num in nums[1:]:
            prev = num + max(0,prev)
            m = max(m,prev)
        return m
