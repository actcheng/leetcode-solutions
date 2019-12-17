# Problem 15
# Date completed: 2019/12/18 

# 756 ms (84%)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums)-2 and nums[i] <= 0:
            if i > 0 and nums[i] == nums[i-1]: 
                i+= 1
                continue
                
            left, right = i+1, len(nums)-1
            while left < right:
                three_sum = nums[i]+nums[left]+nums[right]
                if three_sum == 0:                         
                        res.append([nums[i],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1
            i += 1
        return res

