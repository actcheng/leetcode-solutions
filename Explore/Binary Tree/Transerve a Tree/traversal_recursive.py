# Date: 2019/09/04

# 1. Preorder: Root -> Left -> Right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        arr = []           
        def leaves(node): 
            if not node: return
            arr.append(node.val)
            leaves(node.left)
            leaves(node.right)            
        leaves(root)
        return arr
        
     
# 2. In-order: Left -> Root -> Right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        arr = []
        def leaves(node):
            if not node: return
            if node.left: leaves(node.left)
            arr.append(node.val)
            if node.right: leaves(node.right)
        leaves(root)
        return arr
 
# 3. Post-order: Left -> Right -> Root
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        arr = []
        def leaves(node):
            if not node: return
            if node.left: leaves(node.left)            
            if node.right: leaves(node.right)
            arr.append(node.val)
        leaves(root)
        return arr
