# Problem 66
# Date completed: 2019/09/26

# 36 ms

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[-(i+1)] += 1
            if digits[-(i+1)] <= 9: 
                return digits
            else:
                digits[-(i+1)] = 0
                
        return [1]+digits
