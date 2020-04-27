# Problem 1143
# Date completed: 2020/04/27 

# 920 ms (17%)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        m = [[0]*l1 for i in range(l2)]
        
        for i in range(l2):
            for j in range(l1):
                
                if text1[j] == text2[i]:
                    m[i][j] = 1 + m[max(0,i-1)][max(0,j-1)]
                else:
                    m[i][j] = max(m[max(0,i-1)][j], m[i][max(0,j-1)])
                m[i][j] = min([m[i][j],i+1,j+1])
        
        return m[-1][-1]
        
        
# Sample solution (296 ms)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # If text1 doesn't reference the shortest string, swap them.
        if len(text2) < len(text1):
            text1, text = text2, text1
        
        
        # The previous column starts with all 0's and like before is 1
        # more than the length of the first word.
        previous = [0] * (len(text1) + 1)
        
        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            # Create a new array to represent the current column.
            current = [0] * (len(text1) + 1)
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            # The current column becomes the previous one.
            previous = current
        
        # The original problem's answer is in previous[0]. Return it.
        return previous[0]
