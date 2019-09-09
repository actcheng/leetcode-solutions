# Problem 700
# Date: 2019/09/09

# 88 ms, Recursive
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if val == root.val: 
            return root
        elif val > root.val and root.right:
                return self.searchBST(root.right,val)
        elif root.left: return self.searchBST(root.left,val)
        
        return None
        
# 88 ms, Iterative
def searchBST(self, root: TreeNode, val: int) -> TreeNode:

    node = None
    while root and not node:
        if val == root.val: 
            node = root
        elif val > root.val:
            root = root.right
        else:
            root = root.left

    return node

# Should be faster
def searchBST(self, root: TreeNode, val: int) -> TreeNode:

    while root:
        if val == root.val: 
            break
        elif val > root.val:
            root = root.right
        else:
            root = root.left

    return root
