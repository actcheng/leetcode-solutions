# Problem 701
# Date: 2019/09/09

# 124 ms, recursive
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        
        return root

# 124 ms, iterative
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        node = root
        while True:
            if val > node.val:
                if node.right:
                    node = node.right
                else: 
                    node.right = TreeNode(val)
                    break
            else:
                if node.left:
                    node = node.left
                else: 
                    node.left = TreeNode(val)
                    break
        
        return root
