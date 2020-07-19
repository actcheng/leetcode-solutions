# Problem 662
# Date completed: 2020/07/09

# 2980 ms 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        
        res = 0
        this_level = [root]
        next_level = []
        
        while this_level:
            
            while this_level and this_level[0] == None:
                this_level.pop(0)
                
            while this_level and this_level[-1] == None:
                this_level.pop()
            
            res = max(res,len(this_level))
            # print([node.val if node else None for node in this_level], len(this_level))
            
            for node in this_level:
                next_level.append(node.left if node else None)
                next_level.append(node.right if node else None)
            
            this_level, next_level = next_level, []
            
            
            
        return res

