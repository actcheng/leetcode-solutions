# Problem 137
# Date completed: 2020/06/22

# 60 ms, 58%
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        store = set([])
        total, unique_total = 0, 0
        for num in nums:
            total += num
            if num not in store:
                store.add(num)
                unique_total += num
                
        return (unique_total*3-total) // 2

