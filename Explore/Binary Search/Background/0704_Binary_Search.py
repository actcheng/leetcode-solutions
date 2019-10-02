# Problem 704
# Date completed: 2019/10/02 

# 296 ms (22%)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        
        l, h = 0, len(nums)-1
        mid = l + (h-l)//2
        if nums[mid] == target: return mid
        while h > l:
            if nums[mid] < target:
                l = mid+1                
            else:
                h = mid-1
            mid = l + (h-l)//2
            if nums[mid] == target: return mid
        return -1
        
