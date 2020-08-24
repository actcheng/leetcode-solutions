# Problem 1389
# Date completed: 2020/08/24 

# 22 ms (93%)
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        arr = [nums.pop(0)]
        index.pop(0)
        
        while nums:
            num, ind = nums.pop(0), index.pop(0)
            arr.insert(ind,num)

        return arr
            
        
