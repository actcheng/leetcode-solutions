# Problem 34
# Date completed: 2019/10/03 

# 80 ms (10%)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1,-1]
        
        if len(nums)==1: return [0,0] if nums[0] == target else [-1,-1]

        l,r = 0, len(nums)-1

        while l+1<r:
            mid = (l+r)//2
            if nums[mid] == target:
                ans =  [min(mid,l+self.searchRange(nums[l:mid+1],target)[0]),
                        max(mid,mid+self.searchRange(nums[mid:r+1],target)[1])]
                return ans
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
        
        if nums[l] == nums[r] == target:
            return [l,r]
        elif nums[l] == target:
            return [l,l]
        elif nums[r] == target:
            return [r,r]
        else: 
            return [-1,-1]
            
 # 56 ms sample solution
 class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if not nums:
            return [-1, -1]

        # Find left
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        left = l if l >= 0 and l < len(nums) and nums[l] == target else -1

        # Find right
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        right = r if r >= 0 and r < len(nums) and nums[r] == target else -1

        return [left, right]
 
