# Problem 153
# Date completed: 2019/10/03 

# 28 ms (56%)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return
        
        l, r = 0, len(nums)-1
        while l+1<r:
            mid = (l+r)//2
            if nums[l]<nums[mid]: 
                if nums[mid] < nums[r]: # No pivot
                    return nums[l]
                elif nums[mid] > nums[mid+1]: # Pivot on right
                    l = mid+1
                else:
                    l = mid
            else: # Pivot on left
                r = mid
        return nums[l] if nums[l]<nums[r] else nums[r]
                
