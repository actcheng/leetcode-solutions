# Problem 559 
# Date: 2019/09/14

# 559 ms
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root: return 0
        if not root.children:
            return 1
        else:
            return max([self.maxDepth(child) for child in root.children])+1
