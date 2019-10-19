# Problem 543
# Date completed: 2019/10/19 

# 48 ms (92%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        def helper(node,depth):
            if not node: return depth
            leftDepth, rightDepth = helper(node.left,depth), helper(node.right,depth)
            self.diameter = max(self.diameter,leftDepth+rightDepth)
            # print('diameter', self.diameter)
            depth = max(leftDepth,rightDepth)+1
            # print(node.val,depth, leftDepth,rightDepth)
            return depth
        helper(root,0)
        return self.diameter
