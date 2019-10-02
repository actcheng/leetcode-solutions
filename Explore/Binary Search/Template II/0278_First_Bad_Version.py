# Problem 278
# Date completed: 2019/10/02 

# 20 ms (38%)
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r = 1, n
        while l<r:
            mid = (l+r)//2
            res = isBadVersion(mid)            
            if res: # Search left, including this version
                r = mid                
            else: # Search right
                l = mid + 1
        return r    
