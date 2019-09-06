# Problem 112
# Date: 2019/09/05

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int, prevSum = 0) -> bool:
        if root:            
            prevSum += root.val
            if not (root.left or root.right):
                return prevSum == sum
            return ((root.left and self.hasPathSum(root.left, sum, prevSum)) or 
                    (root.right and self.hasPathSum(root.right, sum, prevSum)))  
        else:
            return False
