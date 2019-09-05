# Date: 2019/09/05

# Recursive solution

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def checkSide(leftNode,rightNode):
            if leftNode and rightNode:
                return leftNode.val == rightNode.val and checkSide(rightNode.left,leftNode.right) and checkSide(leftNode.left,rightNode.right)
            elif not leftNode and not rightNode:
                return True
            else:
                return False      
            
        if not root:  
            return True
        
        return  checkSide(root.left,root.right)
