# Date completed: 2020/04/30 

# 112 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root or root.val != arr[0]: return False
        if len(arr) == 1: return (not root.left and not root.right)
        
        self.end = len(arr)-1
        self.stack = [[root,0]]
        
        def check_node(node,ind):
            if node and node.val == arr[ind]:
                if ind < self.end: # Not yet ended
                    self.stack.append([node,ind])
                else: # Check if leaf node
                    if not node.left and not node.right:
                        return True
                
            return False              

        while self.stack:
            node, ind = self.stack.pop()
            if check_node(node.left,ind+1) or check_node(node.right,ind+1): return True                    
            
        return False
