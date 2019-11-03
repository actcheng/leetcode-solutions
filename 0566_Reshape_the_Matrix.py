# Problem 566 
# Date completed: 2019/11/03

# 124 ms (33%)
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums or not nums[0]: return nums
        
        h,w = len(nums), len(nums[0])
        if h*w != r*c: return nums
        n = 0
        res = []
        for i in range(r):
            res.append([])
            for j in range(c):
                res[i].append(nums[n//w][n%w])
                n += 1
                
        return res
