# Problem 100
# Date completed: 2019/09/24 


# 36 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not (p and q): return not (p or q)
        if p.val != q.val: return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

# 2019/11/15
# Iterative
# 28 ms (95%)

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True

        stack = [(p,q)]
        while stack:
            a, b = stack.pop()
            if (a and not b) or (b and not a): return False
            if a.val != b.val: return False
            if a.left or b.left:  stack.append((a.left,b.left))
            if a.right or b.right: stack.append((a.right,b.right))
                
        return True    
