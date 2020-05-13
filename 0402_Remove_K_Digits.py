# Problem 402
# Date completed: 2020/05/13 

# 532 ms (8%)
# How to improve?
# - Use stack (or other methods) for removing the digits
# - Compare the str instead of int

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k: return "0"
        
        digits = [int(digit) for digit in list(num)]
        i = 0
        while k > 0:
            
            # Find digit to remove
            while i < len(digits)-1:
                if digits[i+1] >= digits[i]:
                    i += 1
                else:
                    break
            
            # Remove digit
            digits = digits[:i] + digits[i+1:]
            k -= 1
            i = max(0,i-1)
            
            # Remove zeros
            while digits and digits[0] == 0: digits.pop(0)            
            if len(digits) <= k: return "0"
            

        return "".join(str(digit) for digit in digits)

