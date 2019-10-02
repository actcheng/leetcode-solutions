# Problem 374
# Date completed: 2019/10/02 

# 16 ms (67%)
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(l,r):
            if r==l: return r
            mid = (l+r)//2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                return helper(l,mid-1)
            else:
                return helper(mid+1,r)
            
        return helper(1,n)
