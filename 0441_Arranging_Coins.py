# Problem 441
# Date completed: 2018/07/15

# 52 ms
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = max(int(round((n*2)**(0.5)))-2,0)
        while n >= k*(k+1)/2:
            k+=1
        return k-1
