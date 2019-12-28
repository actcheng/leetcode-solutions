# Problem 1071
# Date completed: 2019/12/28 

# 28 ms (87%)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1)>len(str2): str1, str2 = str2,str1
            
        def checkDivisible(x,string):
            return x*(len(string)//len(x)) == string
        
        l1,l2 = len(str1),len(str2)
        for i in range(1,l1+1):    
            if (l1%i==0):
                j = l1//i
                if (l2%j==0 and 
                checkDivisible(str1[:j],str1) and 
                checkDivisible(str1[:j],str2)):
                    return str1[:j]
        
        return ''
