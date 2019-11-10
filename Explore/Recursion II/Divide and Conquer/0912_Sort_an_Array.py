# Problem 912
# Date completed: 2019/11/10 

# 488 ms (9%)
# Merge sort, top-down
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l < 2: return nums
        
        list1, list2 = self.sortArray(nums[:l//2]), self.sortArray(nums[l//2:])
        
        merged = []
        while list1 and list2:
            if list1[0] <=  list2[0]:
                merged.append(list1[0])
                list1.pop(0)
            else:
                merged.append(list2[0])
                list2.pop(0)

        merged += list1 if list1 else list2
        return merged
