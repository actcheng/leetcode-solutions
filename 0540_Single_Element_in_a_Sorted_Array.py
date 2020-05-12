# Problem 540
# Date completed: 2020/05/12 

# 72 ms (70%)

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        l, r = 0, len(nums)-1
        while l+1 < r:
            mid = (l+r) // 2

            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            
            if mid % 2:
                if nums[mid] == nums[mid-1]:
                    l = mid
                else:
                    r = mid
            else:
                if nums[mid] == nums[mid-1]:
                    r = mid
                else:
                    l = mid

        return nums[l] if l == 0 else nums[r]
