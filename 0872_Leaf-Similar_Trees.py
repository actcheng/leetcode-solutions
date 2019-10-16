# Problem 872
# Date completed: 2019/10/16

# 36 ms (87%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        if not root1 and not root2: return True
        if not (root1 and root2): return False
        
        def findLeaves(root):
            #DFS
            stack = [root]
            leaves = []
            while stack:    
                node = stack.pop()
                if not (node.left or node.right):
                    leaves.append(node.val)
                else:
                    if node.right: stack.append(node.right)
                    if node.left: stack.append(node.left)
                    
            return leaves
        
        leaves1 = findLeaves(root1)
        leaves2 = findLeaves(root2)
        if len(leaves1) != len(leaves2):
            return False
        else:
            return all(leaves1[i] == leaves2[i] for i in range(len(leaves1)))
