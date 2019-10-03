# Problem 1108
# Date completed: 2019/10/03

# 12 ms (87%)
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.','[.]')
        # return '[.]'.join(address.split('.'))
