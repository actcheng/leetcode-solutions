# Problem 46
# Date completed: 2019/10/01 

# 48 ms (72%)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<2: return [nums]
        ans = []
        for i in range(len(nums)):
            arrs = [[nums[i]]+arr for arr in self.permute(nums[:i]+([] if i>=len(nums)-1 else nums[i+1:]))]
            ans.extend(arrs)
        return ans
