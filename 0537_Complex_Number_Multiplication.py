# Problem 537
# Date completed: 2018/07/15

# 20 ms (100%)
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_real=int(a.split('+')[0])
        a_img=int(a.split('+')[1][:-1])
        b_real=int(b.split('+')[0])
        b_img=int(b.split('+')[1][:-1])
        c_real=a_real*b_real-a_img*b_img
        c_img=a_real*b_img+a_img*b_real
        return str(c_real)+'+'+str(c_img)+'i'
