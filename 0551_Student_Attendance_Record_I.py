# Problem 551
# Date completed: 2019/09/01

# 28 ms
class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = False
        len_s = len(s)
        for i in range(len_s):
            x = s[i]
            if x == 'A':
                if absent:
                    return False
                else:
                    absent = True
            elif x == 'L':
                if i < len_s-2 and s[i+1:i+3] == 'LL':
                    return False
                
        return True
