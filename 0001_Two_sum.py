# Problem #1
# Date completed: 2018/07/04
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if (nums[i]+nums[j]==target and i!=j):
                    return [i,j]

                class Solution:

# Date completed: 2019/04/08
# 1200 ms
def twoSum(self, nums: List[int], target: int) -> List[int]:
    ans = [i for i in range(len(nums)) if target-nums[i] in nums] 
    if len(ans) > 2:
        ans.remove(nums.index(int(target/2)))
    return  ans
