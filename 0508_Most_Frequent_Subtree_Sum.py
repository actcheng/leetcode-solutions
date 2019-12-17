# Problem 508
# Date completed: 2019/12/18 

# 44 ms (89%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        counts = {}
        
        def findSubtreeSum(node):
            if not node: return 0
            s = node.val + findSubtreeSum(node.left) + findSubtreeSum(node.right)
            if s in counts:
                counts[s] += 1
            else:
                counts[s] = 1
            return s
        
        findSubtreeSum(root)
        if len(counts) == 0: return []
        
        max_freq = max(counts.values())
        return [s for s in counts if counts[s] == max_freq]
