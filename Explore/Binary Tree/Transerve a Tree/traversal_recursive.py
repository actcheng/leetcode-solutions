
# Date: 2019/09/04
# Problem 144
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
        
# Problem 94     
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

# Problem 145    
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

# Problem 102
# 4. Level-order: [[level 1], [level 2], [level 3]]
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        arr = []
        queue = [[0, root]]        
        while len(queue) > 0:
            level, root = queue.pop(0)  
            if not root: continue
            if root.left: queue.append([level+1, root.left])
            if root.right: queue.append([level+1, root.right])
            if len(arr) < level+1: arr.append([])
            arr[level].append(root.val)
        return arr
