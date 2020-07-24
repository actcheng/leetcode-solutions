# Problem 260
# Date completed: 2020/07/23

# 50 ms (91%)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        res = set([])
        
        for num in nums:
            if num in res:
                res.remove(num)
            else:
                res.add(num)
                
        return list(res)
