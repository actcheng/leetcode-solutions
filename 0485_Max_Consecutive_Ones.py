# Problem 485
# Date completed: 2019/09/12

# 416 ms
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = count = 0
        for n in nums:
            if n == 0:
                maxOnes = max(maxOnes, count)
                count = 0
            else:
                count += 1                
                
        return max(maxOnes,count)
