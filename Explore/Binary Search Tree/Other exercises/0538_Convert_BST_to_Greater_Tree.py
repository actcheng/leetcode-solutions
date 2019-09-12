# Problem 538  
# Date completed: 2019/09/11

# 88 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        
        if not root: return None
        self.sum = 0
        
        def plusSum(root):
            
            if root.right:
                plusSum(root.right)
            val = root.val
            root.val += self.sum
            self.sum += val
            if root.left:
                plusSum(root.left)
                
            return
        
        plusSum(root)
        
        return root
