# Problem 58
# Date completed: 2018/12/26

# 64ms
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        try:
            return len(s.strip(' ').split(' ')[-1])
        except:
            return 0
          

# 44ms
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        try:
            found = False
            i = 1
            s = s.strip(' ')
            while not found and i<len(s):
                if s[-i] != ' ':
                    i += 1
                else:
                    found=True
            if not found:
                return len(s)
            return i-1
        except:
            return 0
