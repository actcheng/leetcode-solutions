# Problem 273
# Date completed: 2019/10/06 

# 44 ms (25%)
# A bit slow but I think the code is cleaner

class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0: return "Zero"
        
        words = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five",
                 6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",
                 11:"Eleven",12:"Twelve",13:"Thirteen",
                 14:"Fourteen",15:"Fifteen",16:"Sixteen",
                 17:"Seventeen",18:"Eighteen",19:"Nineteen",
                 20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",
                 60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",
                 100:"Hundred",1000:"Thousand",1000000:"Million",
                 1000000000:"Billion"}
        
        nums = list(words.keys())
        nums.reverse()
        end = len(nums)
        res = []
        def getWords(num,start):
            for i in range(start,end):
                 if num >= nums[i]:
                        mod = num // nums[i]
                        num = num % nums[i]
                        if mod > 1:
                            getWords(mod,i)
                        elif i<4:
                            res.append('One')
                        res.append(words[nums[i]])
        getWords(num,0)
        
        return ' '.join(res)
