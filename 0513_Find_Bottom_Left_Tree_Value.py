# Problem 513
# Date completed: 2019/10/17 

# 52 ms (69%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root: return
        
        # BFS
        left = root.val
        this_level = [root]
        next_level = []
        while this_level or next_level:            
            if not this_level:
                this_level, next_level = next_level, []
                left = this_level[0].val
            else:                
                node = this_level.pop(0)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
        
        return left
