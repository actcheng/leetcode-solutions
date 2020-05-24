# Problem 1008
# Date completed: 2020/05/24 

# 36 ms (64%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder: return None
        head = TreeNode(preorder.pop(0))
        path = [head]

        while preorder:
            val = preorder.pop(0)
            new = TreeNode(val)
            if val < path[-1].val:
                path[-1].left = new                
            else:
                for i in range(len(path)):
                    if not path[i].right and val > path[i].val:
                        break
                path = path[:i+1] 
                path[-1].right = new
            path.append(new)               
                
        return head
