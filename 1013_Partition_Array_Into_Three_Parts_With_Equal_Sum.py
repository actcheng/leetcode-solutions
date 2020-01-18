# Problem 1013
# Date completed: 2020/01/18 

# 348 ms (33%)
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total%3 != 0: return False
        target = total // 3
        part_sum = 0
        parts = 0
        for num in A:
            part_sum += num
            if part_sum == target:
                parts += 1
                part_sum = 0
            
        return parts == 3 and part_sum == 0
