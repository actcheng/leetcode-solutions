# Problem 100
# Date completed: 2019/09/24 


# 36 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not (p and q): return not (p or q)
        if p.val != q.val: return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
