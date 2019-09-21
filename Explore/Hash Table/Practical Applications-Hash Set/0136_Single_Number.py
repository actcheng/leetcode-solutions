# Problem 136 
# Date completed: 2019/09/21

# 112 ms
class Solution:
    def singleNumber(self, nums):
        hashset = set()
        for i in nums:
            if i in hashset:
                hashset.remove(i)
            else:
                hashset.add(i)
        return list(hashset)[0]
