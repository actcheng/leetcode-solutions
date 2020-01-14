# Problem 1022
# Date completed: 2020/01/14 

# 36 ms (61%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        self.total = 0
        
        def dfs(node,value):
            value = (value << 1) + node.val

            if not (node.left or node.right):
                self.total += value
            else:
                if node.left: dfs(node.left,value)
                if node.right: dfs(node.right,value)
                    
        dfs(root,0)
        return self.total
