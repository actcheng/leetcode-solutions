# Problem 201
# Date completed: 2020/04/24 

# 64 ms (35%)
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        m_b = list(bin(m).split('b')[-1])
        
        r_b = []
        top = 2**(len(m_b)-1)
        low = 0
        while m_b:            
            
            if m_b.pop(0) == '1':
                low += top
                if n < low + top:
                    r_b.append('1')
                else:
                    r_b.append('0')
            else:
                r_b.append('0')
            
            # print(low, top)
            # print(m_b,r_b)
            top = top >> 1


        return int(''.join(r_b),2)
