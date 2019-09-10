# Problem 665
# Date completed: 2019/09/10

# 208 ms
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        l = len(nums)
        for i in range(l-1):
            if nums[i+1] < nums[i]:
                if not modified:
                    # Try to modify to fix i-1 to i+1
                    # print(nums[i+2], nums[i+1], nums[i], nums[i-1], i, l-2)
                    if (i == 0 or i == l-2 or 
                        nums[i+1] > nums[i-1] or 
                        nums[i+2] >= nums[i]):
                        modified = True
                    else: 
                        return False
                else:
                    return False
        return True
