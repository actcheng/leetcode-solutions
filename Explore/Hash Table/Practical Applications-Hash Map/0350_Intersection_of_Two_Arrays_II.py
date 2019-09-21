# Problem 350
# Date completed: 2019/09/21

# 76 ms
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        repeated = set(nums1) & set(nums2)
        if not repeated: return 
        res = []
        for x in repeated:
            res.extend([x]*(min(nums1.count(x),nums2.count(x))))
        return res


# Sample solution:
# 44 ms
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        numbers = dict()
        for num in nums1:
            if num in numbers:
                numbers[num] +=1
            else:
                numbers[num] = 1
        for num in nums2:
            if num in numbers and numbers[num]>0:
                ans.append(num)
                numbers[num]-=1
        return ans
