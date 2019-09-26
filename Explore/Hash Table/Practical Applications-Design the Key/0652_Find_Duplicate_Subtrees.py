# Problem 652
# Date completed: 2019/09/27 

# 80 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.subtrees = {}
        self.dup = []
        def serial(root):
            if not root: return 'null'
            if root.left or root.right:
                res = '{}({},{})'.format(root.val,serial(root.left),serial(root.right))
            else:
                res = '({})'.format(root.val)
            if res in self.subtrees:
                if self.subtrees[res]: 
                    self.dup.append(self.subtrees[res])
                    self.subtrees[res] = None
            else:
                self.subtrees[res] = root
            return res
        
        serial(root)
        return self.dup
