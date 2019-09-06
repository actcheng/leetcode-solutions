# Problem 106
# Date: 2019/09/06

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        ind = inorder.index(root.val)
        # Cannot swap the order: postorder is public -> need to be used to build right tree first!        
        root.right = self.buildTree(inorder[ind+1:],postorder)
        root.left = self.buildTree(inorder[:ind],postorder)
        
        return root

# Can swap order but need more space and slower!  
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        ind = inorder.index(root.val)
            
        root.right = self.buildTree(inorder[ind+1:],postorder[ind:-1])
        root.left = self.buildTree(inorder[:ind],postorder[:ind])
        
        return root
