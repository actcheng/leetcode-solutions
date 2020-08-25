# Problem 43
# Date completed: 2020/08/24

# 160 ms (37%)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_int = [int(d) for d in num1]
        num2_int = [int(d) for d in num2]
        l1, l2 = len(num1_int), len(num2_int)
        
        def multiply_digit(d):

            res = []
            carry = 0 
            for i in range(l1-1,-1,-1):
                prod = d * num1_int[i] + carry
                res.insert(0,prod%10)
                carry = prod // 10
                
            if carry > 0: res.insert(0,carry)
            return res
        
        def add_results(prev,new,shift):
            prev, res = prev[:-shift], prev[-shift:]
            # print(new,prev)
            carry = 0
            while new and prev:
                sum = new.pop() + prev.pop() + carry
                res.insert(0,sum%10)
                carry = sum // 10
                
            while carry > 0 and new:
                sum = new.pop() + carry
                res.insert(0,sum%10)
                carry = sum // 10
                
            if carry > 0: res.insert(0,carry)
            if new: res = new + res
                
            return res
            
            
        ans = None
        for i in range(l2-1,-1,-1):
            # print(num2_int[i], multiply_digit(num2_int[i]))
            if ans == None: 
                ans = multiply_digit(num2_int[i])
            else:
                ans = add_results(ans,multiply_digit(num2_int[i]),l2-i-1)
            # print(ans)
        
        while len(ans) > 1 and ans[0] ==0: ans.pop(0)
        
        return ''.join([str(d) for d in ans])


