# Problem 1110
# Date completed: 2019/10/01 

# 92 ms (14%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        queue = [[root,None,False]]
        while queue:
            node, parent, isLeft = queue.pop(0)
            if node.val in to_delete: 
                if parent:
                    if isLeft: 
                        parent.left = None
                    else:
                        parent.right = None
                 
                to_delete.remove(node.val)
                if node.left: queue.append([node.left,None,False])
                if node.right: queue.append([node.right,None,False])
            else:
                if not parent: ans.append(node)
                if node.left: queue.append([node.left,node,True])
                if node.right: queue.append([node.right,node,False])
        return ans
                
# 68 ms solution using recursion
class Solution:
    
    def delNodes(self, root, to_delete):
        to_delete_set = set(to_delete)
        res = []

        def helper(root, is_root):
            if not root: return None
            root_deleted = root.val in to_delete_set
            if is_root and not root_deleted:
                res.append(root)
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root
        helper(root, True)
        return res
    
