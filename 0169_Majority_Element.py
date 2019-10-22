# Problem 169
# Date completed: 2019/10/22 

# 204 ms (40%)
# Boyer-Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if count == 0:
                prefix = num
                count += 1
            else:
                count +=  1 if num==prefix else -1
        
        return prefix
