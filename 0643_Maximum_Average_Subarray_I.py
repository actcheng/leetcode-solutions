# Problem 643
# Date completed: 2019/09/25 

# 988 ms
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = Sum = sum(nums[0:k])
        for i in range(len(nums)-k):
            Sum += nums[i+k]-nums[i]
            maxSum = max(maxSum,Sum)
        return maxSum / k
