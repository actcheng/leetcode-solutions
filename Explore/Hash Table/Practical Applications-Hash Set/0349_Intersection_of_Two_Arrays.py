# Problem 349 
# Date completed: 2019/09/21

# 56 ms
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
