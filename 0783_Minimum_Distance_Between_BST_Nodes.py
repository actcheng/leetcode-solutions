# Problem 783
# Date completed: 2019/11/16

# 32 ms (93%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        minDiff = None
        prev = None      
            
        self.stack = []
        
        def appendLeftLeaves(node):
            while node:
                self.stack.append(node)
                node = node.left
                
        appendLeftLeaves(root)
        
        while self.stack:
            node = self.stack.pop()
            if prev != None: 
                minDiff = (minDiff and min(minDiff,node.val-prev)) or node.val-prev
            prev = node.val
            
            if node.right:
                appendLeftLeaves(node.right)
                    
        return minDiff

        
