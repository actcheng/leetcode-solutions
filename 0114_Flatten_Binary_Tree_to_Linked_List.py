# Problem 114
# Date completed: 2020/08/24 

# 40 ms (74%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        
        stack = [root]
        current = None
        while stack:
            node = stack.pop()
            if current: current.right = node                        
            
            if node.right: 
                stack.append(node.right)
                node.right = None
            if node.left: 
                stack.append(node.left)
                node.left = None
                
            current = node

