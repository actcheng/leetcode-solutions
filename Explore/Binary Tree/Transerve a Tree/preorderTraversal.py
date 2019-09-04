# Date: 2019/09/04

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        arr = []
        self.leaves(root,arr)
        return arr
    
    def leaves(self,node,arr): 
        if not node: return
        arr.append(node.val)
        self.leaves(node.left,arr)
        self.leaves(node.right,arr)
        
