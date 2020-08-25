# Problem 687
# Date completed: 2020/08/24

# 416 ms (87%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        
        def find_depth(node):
            if not node: return 0

            left = find_depth(node.left) 
            right = find_depth(node.right)
            
            if node.left and node.left.val != node.val:  left = 0              
            if node.right and node.right.val != node.val: right = 0

            if left + right > self.res: self.res = left + right 
            # print(node.val, left, right, self.res)
            return max(left, right) + 1
        
        find_depth(root)
        return self.res
