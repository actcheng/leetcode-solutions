# Problem 111
# Date completed: 2019/10/16

# 48 ms (88%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        
        # BFS
        queue = [[root,0]]
        while queue:
            node,level = queue.pop(0)
            if not (node.left or node.right): return level+1
            if node.left: queue.append([node.left,level+1])
            if node.right: queue.append([node.right,level+1])
                
