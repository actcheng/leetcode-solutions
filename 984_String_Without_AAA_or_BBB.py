# Problem 984
# Date completed: 2019/10/28

# 32 ms (93%)
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if A==B: return 'ab'*A

        nums = [A,B] if A > B else [B,A]
        letters = ['a','b'] if A > B else ['b','a']
        
        counts0 = nums[0] // 2
        counts1 = nums[1] - counts0
        if counts1 < 0: counts0, counts1 = counts0-1, 0
            
        print(counts0,counts1)
        res = ('' + 
               ''.join([letters[0],letters[1]])*counts1*2 +
               ''.join([letters[0]*2,letters[1]])*(nums[1]-counts1*2) +  
               letters[0]*(nums[0]-counts0*2))
        
        return res
