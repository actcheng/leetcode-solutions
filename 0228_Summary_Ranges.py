# Problem 228
# Date completed: 2019/10/09 

# 36 ms (68%)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return
        if len(nums)==1: return [str(nums[0])]
        ranges = []
        minNum, maxNum = nums[0], nums[0]        
        for num in nums[1:]:
            if num != maxNum+1:
                ranges.append(str(minNum) if maxNum==minNum else f'{minNum}->{maxNum}')
                minNum = num
            maxNum = num
            
        ranges.append(str(minNum) if maxNum==minNum else f'{minNum}->{maxNum}')
        
        return ranges
