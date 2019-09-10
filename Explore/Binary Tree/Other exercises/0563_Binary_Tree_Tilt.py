# Problem 563  
# Date: 2019/09/10

# 64 ms
class Solution:
    def findTilt(self, root: TreeNode) -> int:        
        
        self.tilt = 0        
        def helper(root):
            if not root: return 0
            
            sumLeft = helper(root.left)
            sumRight = helper(root.right)
            
            self.tilt += abs(sumLeft - sumRight)
            return sumLeft+sumRight+root.val
        
        helper(root)
        
        return self.tilt
