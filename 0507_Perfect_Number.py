# Problem 507
# Date completed: 2020/01/18 

# 32 ms (79%)
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1: return False
        total = 0
        max_num = int(num**(1/2))
        for i in range(1,max_num+1):
            if num%i == 0:
                total += i
                if i>1 and num//i != i :
                    total += num//i
                if total>num: return False

        return total == num
