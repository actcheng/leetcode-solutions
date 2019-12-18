# Problem 226
# Date completed: 2019/12/18 

# 24 ms (95%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)        
        return root
