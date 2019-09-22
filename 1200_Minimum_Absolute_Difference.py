 Problem 1200
# Date completed: 2019/09/22 

# 420 ms
class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        diff = [arr[i+1]-arr[i] for i in range(len(arr)-1)]
        minDiff = min(diff)
        return [[arr[i],arr[i+1]] for i in range(len(diff)) if diff[i]==minDiff]
