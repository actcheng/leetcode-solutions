# Problem 628
# Date completed: 2020/01/18 

# 280 ms (59%)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:        
        nums.sort()
        if nums[-1] < 0 or nums[0]*nums[1] < 0:
            return nums[-3]*nums[-2]*nums[-1]
        else:
            return nums[-1]*max(nums[0]*nums[1],nums[-3]*nums[-2])
