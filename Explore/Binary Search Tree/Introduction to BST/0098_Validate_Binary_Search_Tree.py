# Problem 98
# Date: 2019/09/08

# 40 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        
        def checkBST(root,minimum,maximum):
            left = right = True
            if root.left:         
                # print('Left',root.val, minimum, root.left.val,  root.left.val >= root.val or (minimum and root.left.val<=minimum))
                if root.left.val >= root.val or (minimum and root.left.val<=minimum): return False
                left = checkBST(root.left, minimum, root.val)
            if root.right:
                # print('Right',root.val, maximum, root.right.val, root.right.val <= root.val or (maximum and root.right.val>=maximum))
                if root.right.val <= root.val or (maximum and root.right.val>=maximum): return False
                right = checkBST(root.right, root.val,maximum)

            return left and right
        
        return checkBST(root,None,None)
    
