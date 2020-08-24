# Problem 1539
# Date completed: 2020/08/24 

# 52 ms (82%)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]: return k
        
        k -= (arr[0]-1)
        for i in range(len(arr)-1):
            missing = arr[i+1] - arr[i] -1
            if missing == 0: continue
            if k - missing <= 0:
                return arr[i] + k
            k -= missing
            
        return arr[-1] + k
