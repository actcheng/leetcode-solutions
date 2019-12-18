# Problem 442
# Date completed: 2019/12/19 

# 364 ms (96%)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set(nums)
        for n in nums:
            if n not in res: 
                res.add(n)
            else:
                res.remove(n)
        return list(res)
