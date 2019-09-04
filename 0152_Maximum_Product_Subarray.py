# Problem 152
# Date completed: 2019/09/04

# 120 ms
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = max(nums)
        arr = nums
        j = 1
        while (len(arr) > 1 and 
               not (max(arr)==0 and min(arr)==0) and 
               ((abs(min(nums[j:]))>1 or max(nums[j:])>1) or abs(min(arr))>largest)):
            arr = [arr[i]*nums[i+j] for i in range(len(arr)-1)]            
            largest = max(largest, max(arr))            
            j += 1
            # print(largest,max(arr), arr,nums[j:])
        return largest
            
# Solution to learn from:
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxValue = minValue = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            one = maxValue*nums[i]
            two = minValue*nums[i]
            maxValue = max(one, two, nums[i])
            minValue = min(one, two, nums[i])
            res = max(res, maxValue)
        return res
