# Problem 401 
# Date completed: 2019/09/19

# 2112 ms
# very slow, use bitwise!!
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:        
        
        if not num or num==0: return ["0:00"]
        if num > 8: return 
        
        intervals = [1,2,4,8,16,32,1*60,2*60,4*60,8*60]
        times = [[i//60,i%60,[i]] for i in intervals]

        for j in range(num-1):
            times = [[t[0]+i//60,t[1]+i%60,t[2]+[i]] for i in intervals for t in times if i not in t[2] and t[0]+i//60 < 12 and t[1]+i%60 <60]

        return list(set(["{}:{}".format(t[0],str(t[1]).zfill(2)) for t in times]))
    
# 32 ms solution to learn from
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ans = []
        for i in range(1024):
            if bin(i).count('1') == num and i%64 < 60 and i//64 < 12:
                mn = str(i%64)
                if len(mn) < 2:
                    mn = '0'+ mn
                
                hr = (i//64)
                
                ans.append(str(hr)+":"+mn)
                
        return ans
        
