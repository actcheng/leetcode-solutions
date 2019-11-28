# Problem 384
# Date completed: 2019/11/28 

# 360 ms (65%)
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.orig = list(nums)
        self.nums = nums
        self.len = len(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = list(self.orig)
        return self.nums
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        self.nums = list(self.orig)
        # Shuffle
        for i in range(self.len):
            ind = random.randint(i,self.len-1)
            self.nums[ind], self.nums[i] = self.nums[i], self.nums[ind] 
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
