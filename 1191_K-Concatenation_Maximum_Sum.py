# Problem 1191 
# Date completed: 2019/09/15

# 408 ms
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        if not arr: return 0
        
        arrNew = arr.copy()        
        res = max(arrNew)
        
        if res <= 0: return 0        
        if k > 1: arrNew.extend(arr)
        
        arrSum = 0
        
        for a in arrNew:
            # print(a,res,arrSum)
            arrSum += a            
            res = max(res,arrSum)
            arrSum = max(0,arrSum)
        
        arrSum = sum(arr)
        # print(arrSum, arrSum*k)
        if arrSum > 0: 
            return (k*arrSum+(res-arrSum*2)) % (10**9 + 7)   
        
        return res % (10**9 + 7)
