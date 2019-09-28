# Problem 209
# Date completed: 2019/09/28

# 88 ms
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s: return 0
        if nums[0] >= s: return 1
        l = len(nums)        
        total = nums[0]
        j = 0
        for i in range(1,l):
            total += nums[i]
            # print(i,j,l,total,total>s)
            while total >= s:
                l = min(i-j+1,l)
                total -= nums[j]
                j += 1
                # print(i,j,l,total,total>s)
        return l
