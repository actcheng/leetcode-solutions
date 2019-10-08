# Problem 113
# Date completed: 2019/10/08

# 48 ms (95%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        self.paths = []
        
        def helper(node,path,pathSum):
            if not node: return
            path = path+[node.val]
            pathSum += node.val
            
            if not node.left and not node.right:
                if pathSum == sum: 
                    self.paths.append(path)
                    return
            else:
                if node.left: helper(node.left,path,pathSum)
                if node.right: helper(node.right,path,pathSum)
                    
        helper(root,[],0)
        return self.paths
