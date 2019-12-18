# Problem 238
# Date completed: 2019/12/18 

# 120 ms (95%)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left, right = [1]*l, [1]*l
        for i in range(l):
            left[i] *= nums[i-1]*left[i-1] if i>0 else 1
        for i in range(l-1,-1,-1):
            right[i] *= nums[i+1]*right[i+1] if i<l-1 else 1

        return [left[i]*right[i] for i in range(l)]
        
