# Problem 965
# Date completed: 2019/11/02 

# 40 ms (48%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: return False
        value = root.val
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val != value: return False
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return True
        
