# Problem 287
# Date completed: 2020/06/25

# 88 ms, 26%

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # First cycle
        f, s = nums[0], nums[0]
        while True:
            f = nums[nums[f]]
            s = nums[s]
            if f == s:
                break
                
        # Second cycle
        s = nums[0]
        while f != s:
            f = nums[f]
            s = nums[s]

        return s
