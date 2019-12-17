# Problem 16
# Date completed: 2019/12/17 

# 120 ms (80%)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # a, b, c, d, e
        # ^  b, c, d, e : sum of two of them are closest to target-a, say x
        #    ^1       ^2
        # If ^1 + ^2 > x: move ^2 down
        # If ^1 + ^2 < x: move ^1 up
        # Until ^1+1 = ^2, or ^1+^2 == x        
        l = len(nums)
        nums.sort()        
        output = sum(nums[:3])
        min_diff = target - output
        for i in range(l-2):
            left, right = i+1, l-1
            while left<right:
                diff = target-(nums[i] + nums[left] + nums[right])
                
                if diff == 0:
                    return target
                elif diff>0:
                    left += 1
                else:
                    right -= 1
                    
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    output = target - diff
                    
        return output
