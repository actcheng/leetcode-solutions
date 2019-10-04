# Problem 658
# Date completed: 2019/10/04

# 352 ms (73%)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if arr[0] >= x: return arr[:k]
        if arr[-1] <= x: return arr[-k:]

        l,r = 0, len(arr)-1
        while l +1< r:
            mid = (l+r)//2           
            if arr[mid] == x:
                r = mid
                break
            elif arr[mid] < x:
                l = mid
            else:
                r = mid 
        
        low = max(0, r-k-1)
        high = min(len(arr),r+k)
        while high-low > k:
            if arr[high-1]-x >= x-arr[low]:
                high -= 1
            else:
                low +=1             
        return arr[low:high]
    
