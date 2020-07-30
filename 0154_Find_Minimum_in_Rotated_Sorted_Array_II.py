# Problem 154
# Date completed: 2020/07/25

# 52 ms (85%)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l+1 < r:
            mid = (l+r) // 2
            if nums[l] == nums[mid]:
                return min(self.findMin(nums[l:mid+1]),self.findMin(nums[mid:r+1]))
            elif nums[l] < nums[mid]:
                if nums[mid] <= nums[r]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] <= nums[r]:
                    r = mid
                else:
                    l = mid
        
        return nums[l] if nums[l]<=nums[r] else nums[r]
