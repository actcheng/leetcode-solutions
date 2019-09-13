# Problem 235
# Date: 2019/09/13

# 92 ms
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        
        node = root

        while node.val != p.val and node.val != q.val:
            # print(node.val,p.val,q.val,node.val > p.val,node.val > q.val)            
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                return node           
        
        return node
            
