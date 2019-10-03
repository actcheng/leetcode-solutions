# Problem 162
# Date completed: 2019/10/03 

# 28 ms (87%)
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        if len(nums) < 2: return 0

        l,r = 0, len(nums)-1
        while l<r and r<len(nums):
            mid = (l+r)//2
            if nums[mid]> nums[mid+1]:
                if nums[mid]>nums[mid-1]:
                    return mid
                else:
                    r = mid
            elif nums[mid]< nums[mid+1]:
                l = mid+1
            else:
                l = l + self.findPeakElement(nums[l:mid])
                r = mid+1 + self.findPeakElement(nums[mid+1:max(r+1,len(nums)-1)])
                break
                
        return l if nums[l] > nums[r] else r
    
