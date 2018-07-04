# Problem #3
# Date completed: 2018/07/04

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        letter = ''
        for i in range(len(s)):
            if s[i] in letter:                
                if (letter.index(s[i])+1<=len(letter)):
                    letter=letter[letter.index(s[i])+1:]
            letter += s[i]
            maxlen=max(maxlen,len(letter))
            
        return maxlen
    
