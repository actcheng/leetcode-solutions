# Problem 47
# Date completed: 2019/10/01 

# 724 ms (11%)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<2: return [nums]
        ans = []
        unique = set()
        for i in range(len(nums)):
            arrs = [[nums[i]]+arr
                    for arr in self.permuteUnique(nums[:i]+([] if i>=len(nums)-1 else nums[i+1:])) ]
            for arr in arrs:
                s = str(arr)
                if s not in unique:
                    unique.add(s)
                    ans.append(arr)
        return ans


# 64 ms solution
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, path, res, used):
            if len(path) == len(nums):
                res.append(list(path))
            for i in range (0, len(nums)):
                if not used[i] and (i == 0 or (nums[i] != nums[i - 1] or used[i - 1])):
                    used[i] = True
                    path.append(nums[i])
                    helper(nums, path, res, used)
                    used[i] = False
                    path.pop()
        nums.sort()
        path, res, used = [], [], [False] * len(nums)
        helper(nums, path, res, used)
        return res
