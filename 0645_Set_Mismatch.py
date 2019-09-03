# Problem 645
# Date completed: 2019/09/03

# 256 ms
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        diff = [[num,ind+1] for ind, num in enumerate(nums) if num != ind+1]   
        
        if diff[0][0] > diff[0][1]:
            return [diff[-1][0], diff[0][1]]
        else:
            return [diff[0][0], diff[-1][1]]
            
