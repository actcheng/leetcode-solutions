# Problem 230
# Date completed: 2020/05/20 

# 60 ms (30%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        self.count = 0
        
        def search(node):            

            if not node: return
            res = search(node.left)
            if res != None: return res

            self.count += 1
            if self.count == k: return node.val
            
            return search(node.right)
        
        return search(root)
                
                
