# Problem 989
# Date completed: 2019/10/01 

3 316 ms (94%)
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        carry = 0
        for i in range(len(A)):
            digit, K = K % 10, K // 10
            sum = A[-(i+1)] + digit + carry
            A[-(i+1)], carry = sum % 10, sum // 10
            if K == 0 and carry == 0: break
        
        arr = []      
        while K > 0:
            digit, K = K % 10, K // 10
            sum = digit + carry 
            carry = sum // 10
            arr.append(sum%10)
        
        if carry: arr.append(1)
        arr.reverse()
        
        return arr + A    
