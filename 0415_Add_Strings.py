# Problem 415
# Date completed: 2019/10/01 

# 44 ms (83%)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        x = "0123456789"
        ref = {x[i]:i for i in range(10)}
        
        sumArr = []
        l1, l2 = len(num1), len(num2)
        carry = 0
        for i in range(max(l1,l2)):
            sum =  ((ref[num1[-(i+1)]] if i<l1 else 0) + (ref[num2[-(i+1)]] if i<l2 else 0)) + carry
            carry, digit = sum // 10, sum % 10
            sumArr.append(x[digit])
        if carry == 1: sumArr.append("1")
        sumArr.reverse()
        return ''.join(sumArr)
