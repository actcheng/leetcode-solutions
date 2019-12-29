# Problem 709
# Date completed: 2019/12/29 

# 20 ms (98%)
class Solution:
    def toLowerCase(self, str: str) -> str:
        trans = {chr(i+ord('A')):chr(i+ord('a')) for i in range(26)}
        return ''.join([trans[x] if x in trans else x for x in str])
