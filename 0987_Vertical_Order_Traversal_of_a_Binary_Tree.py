# Problem 987
# Date completed: 2020/08/7

# 36 ms (47%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        columns = collections.defaultdict(list)
        col_this = collections.defaultdict(list)
        
        nodes = [root]
        indices = [0]
        levels = [0]
        current_level = 0
        
        def append_node(node,ind,lvl):
            if not node: return
            nodes.append(node)
            indices.append(ind)
            levels.append(lvl)
        
        def extend_columns(col_this):
            for key in col_this:
                columns[key].extend(sorted(col_this[key]))
            
        while nodes:
            node, ind, lvl = nodes.pop(0), indices.pop(0), levels.pop(0)
            if lvl > current_level:
                extend_columns(col_this)
                col_this = collections.defaultdict(list)
                current_level = lvl
                
            col_this[ind].append(node.val)
            append_node(node.left,ind-1,lvl+1)
            append_node(node.right,ind+1,lvl+1)
                
        extend_columns(col_this)
            
        return [columns[key] for key in sorted(columns.keys())]
