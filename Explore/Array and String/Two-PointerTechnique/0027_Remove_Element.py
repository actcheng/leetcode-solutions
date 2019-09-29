# Problem 27 
# Date completed: 2019/09/17

# 32 ms, fast & slow pointer
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 
        slow = 0
        for i in range(len(nums)):
            if nums[i] != val: 
                nums[slow] = nums[i]
                slow+=1
        return slow
