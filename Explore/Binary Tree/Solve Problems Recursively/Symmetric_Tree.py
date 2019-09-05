# Date: 2019/09/05

# Recursive 

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

# Iterative  

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True
        else:
            queue = [root.left,root.right]

            while queue:
                left = queue.pop(0)
                right = queue.pop(0)
                
                if left and right:
                    if left.val == right.val:
                        queue.append(left.left)
                        queue.append(right.right)
                        queue.append(right.left)
                        queue.append(left.right)
                    else:
                        return False
                elif (not left and right) or (left and not right):
                    return False
            return True
