# Problem 368
# Date completed: 2020/06/13

# 428 ms, 71%
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []
        
        nums.sort()
        max_len = 1
        max_ind = 0
        
        path = nums.copy()
        lens = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            num = nums[i]
            for j in range(i-1,-1,-1):
                if nums[i] % nums[j] == 0 and lens[i] < lens[j]+1:
                    path[i] = j
                    lens[i] = lens[j] + 1
                    if lens[i] > max_len:
                        max_len = lens[i]
                        max_ind = i
                        break
            # print(max_len,max_ind)
            # print(i,path)
            # print(lens)
            
        res = [nums[max_ind] for i in range(max_len)]
        for i in range(max_len-1,-1,-1):
            res[i] = nums[max_ind]
            max_ind = path[max_ind]
            
        return res
