# Problem 724
# Date completed: 2019/09/27

# 176 ms

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0: 
            return -1
        elif l == 1: 
            return 0

        ind = 0
        left, right = 0, sum(nums[1:])
        if left == right: return ind
        for ind in range(1,l):
            left += nums[ind-1]
            right -= nums[ind]
            if left == right: 
                return ind

        return -1
