# Problem 1186
# Date completed: 2019/09/08

# 332 ms
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ignored = notignored = 0
        res = arr[0]
        for a in arr:
            if a >= 0:
                ignored += a
                notignored += a
            else:
                # Ignore previous vs ignore this one
                ignored = max(ignored+a,notignored)
                notignored += a

            if ignored != 0:  res = max(res,ignored)
            if notignored != 0: res = max(res,notignored)

            ignored = max(0,ignored)
            notignored = max(0,notignored)
            
        return max(res,max(arr))
