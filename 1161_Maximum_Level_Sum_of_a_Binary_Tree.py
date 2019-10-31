# Problem 1161
# Date completed: 2019/10/31

# 392 ms (16%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root: return 0
        
        maxSum, maxLevel = root.val, 1
        thisLevel = [root.left,root.right]
        nextLevel = []
        sum = 0
        level = 2
        while nextLevel or thisLevel:
            if not thisLevel:
                print(level,sum)
                if sum > maxSum:
                    maxSum, maxLevel = sum, level
                thisLevel, nextLevel = nextLevel, []
                sum = 0
                level +=1
                
            node = thisLevel.pop(0)
            if node:
                nextLevel.append(node.left)
                nextLevel.append(node.right)
                sum += node.val
                
        return maxLevel
