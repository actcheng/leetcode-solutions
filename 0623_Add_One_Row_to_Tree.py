# Problem 623
# Date completed: 2020/01/19 

# 52 ms (64%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        if d==1:
            new_root = TreeNode(v)
            new_root.left, root = root, new_root
        elif d == 2:
            new_left, new_right = TreeNode(v), TreeNode(v)
            new_left.left, root.left = root.left, new_left
            new_right.right, root.right = root.right, new_right
        else:
            if root.left: root.left = self.addOneRow(root.left,v,d-1)
            if root.right: root.right = self.addOneRow(root.right,v,d-1)
                
        return root
