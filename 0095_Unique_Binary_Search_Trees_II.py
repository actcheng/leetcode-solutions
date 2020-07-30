# Problem 95
# Date completed: 2020/07/30 

# 108 ms (11%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        if n == 0: return []
        
        def helper(nums):            
            
            l = len(nums)
            if l == 0: return [None]
            # print(nums)
            trees = []
            for i in range(l):
                left = helper(nums[:i])
                right = helper(nums[i+1:])
                
                for j in range(len(left)):
                    for k in range(len(right)):
                        trees.append(TreeNode(nums[i]))
                        trees[-1].left = left[j]
                        trees[-1].right = right[k]
                        
            return trees
        
        return helper([i for i in range(1,n+1)])
                        
        
        
