# Problem 257
# Date completed: 2019/12/18 

# 24 ms (98%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.paths = []
        
        def dfs(node,path):
            path = f'{path}->{node.val}' if path else str(node.val)
            if node.left:  dfs(node.left,path)
            if node.right: dfs(node.right,path)
            if not node.left and not node.right: self.paths.append(path)
            return
         
        if root: dfs(root,'')
        
        return self.paths
