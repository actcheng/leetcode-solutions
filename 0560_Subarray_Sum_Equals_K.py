# Problem 560
# Date completed: 2019/10/19 

# 132 ms (57%)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = collections.defaultdict(int)
        sum, count = 0, 0
        for num in nums:
            sum+= num
            if sum == k: count +=1            
            if sum-k in hashmap.keys():
                count += hashmap[sum-k]            
            hashmap[sum] += 1
        return count
        
# Time limit exceeded
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        l = len(nums)
        for i in range(l):
            sum = 0
            for j in range(i,l):
                sum+=nums[j]
                if sum == k: count += 1

        return count

# Recursion (Time limit exceeded)
class Solution:
    def subarraySum(self, nums: List[int], k: int, prevSum=None,end=True) -> int:

        if not prevSum: prevSum = sum(nums)
        num = 1  if prevSum == k else 0          
        if len(nums) == 1: return num
        
        num += self.subarraySum(nums[:-1],k,prevSum=prevSum-nums[-1],end=False)
        if end: num += self.subarraySum(nums[1:],k,prevSum=prevSum-nums[0])
            
        return num
