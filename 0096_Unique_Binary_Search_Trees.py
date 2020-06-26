# Problem 96
# Date completed: 2020/06/24

# 24 ms, 91%
class Solution:
    def numTrees(self, n: int) -> int:
        if n < 1: return 0
        
        nums = [0 for i in range(n+1)]
        nums[0], nums[1] = 1, 1
        
        for i in range(2,n+1):
            for j in range(i):
                nums[i] += nums[j]*nums[i-j-1]
        
        return nums[-1]

