# Problem 437
# Date completed: 2019/10/08 

# 208 ms (65%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        self.count = 0
        
        def helper(node: TreeNode, prevSum: list) -> None:
            if not node: return
            
            prevSum = [num+node.val for num in prevSum] + [node.val]
            self.count += prevSum.count(sum)
            
            if node.left: helper(node.left,prevSum)
            if node.right: helper(node.right,prevSum)
                
            return
        
        helper(root,[])
        
        return self.count
