# Problem 129 
# Date completed: 2019/09/18

# 32 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        def helper(root,prev):
            if not root: return 0
            num = prev*10 + root.val
            if not (root.left or root.right): 
                return num
            else:
                return helper(root.left,num)+helper(root.right,num)           
        
        return helper(root,0)
        
