# Problem 33
# Date completed: 2019/10/02 

# 44 ms (slow)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0,len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[l]<=nums[mid] or nums[r]>=target:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if  nums[r]>nums[mid] or nums[l]<=target:
                    r = mid-1
                else:
                    l = mid+1
        return -1

# 12 ms sample solution
class Solution(object):
    def search(self, nums, target):
        left = 0
        mid = None
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # found
            if nums[mid] == target:
                return mid
            
            # pivot point is on our left
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    # target is on the right, drop the left
                    left = mid + 1
                else:
                    # target is on the left, drop the right
                    right = mid - 1
                
                
            # pivot point is on our right
            elif nums[right] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    # target is on the left, drop the right
                    right = mid - 1
                else:
                    # target is on the right, drop the left
                    left = mid + 1
                
            # data is not pivoted
            
            elif nums[mid] > target:
                # drop the right
                right = mid - 1
                
            elif nums[mid] < target:
                # drop the left
                left = mid + 1

        return -1
