# Problem 190
# Date completed: 2019/11/29 

# 28 ms
class Solution:
    def reverseBits(self, n: int) -> int:    
        bstr = str(bin(n)).split('b')[-1]
        bstr = '0'*(32-len(bstr)) + bstr
        return int(bstr[::-1],2)
        
