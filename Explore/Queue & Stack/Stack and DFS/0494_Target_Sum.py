# Problem 494
# Date completed: 2019/10/25 

# 224 ms (71%)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums: return 0
        dp = collections.defaultdict(int)
        dp[0] += 1

        for i in range(len(nums)):
            next = collections.defaultdict(int)
            for sum in dp:
                next[sum+nums[i]] += dp[sum]
                next[sum-nums[i]] += dp[sum]
            dp = next
            
        return dp[S]
