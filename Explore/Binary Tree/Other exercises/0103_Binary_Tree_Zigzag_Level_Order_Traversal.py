# Problem 103
# Date completed: 2019/09/25

# 44 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        lev = [root]
        trav = []
        levTrav = []
        left = True
        while lev:
            nextLev = []
            levTrav = []
            for i in range(len(lev)):
                node = lev[i] if left else lev[-(i+1)]                
                if node:
                    levTrav.append(node.val)
                    if left:
                        nextLev.append(node.left)
                        nextLev.append(node.right)
                    else:
                        nextLev.append(node.right)
                        nextLev.append(node.left)
            if not left: nextLev.reverse()
            if levTrav: trav.append(levTrav)
            # print(trav,left)
            left = not left
            lev = nextLev
        return trav
