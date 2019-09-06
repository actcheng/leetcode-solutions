# Date: 2019/09/06

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder or not preorder:
            return None

        root = TreeNode(preorder.pop(0))
        ind = inorder.index(root.val)       
        
        root.left = self.buildTree(preorder, inorder[:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        
        return root
