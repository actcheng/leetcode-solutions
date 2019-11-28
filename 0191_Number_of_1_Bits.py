# Problem 191
# Date completed: 2019/11/28 

# 12 ms (93%)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return str(bin(n)).count('1')
