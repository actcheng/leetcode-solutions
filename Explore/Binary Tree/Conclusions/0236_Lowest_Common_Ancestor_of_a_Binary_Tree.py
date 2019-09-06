# Problem 236 
# Date: 2019/09/06

# Very slow
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        paths = {root.val: [root,[]]}     
        def leaves(root,prev): 

            if not root: return            
            paths[root.val] = [root, paths[prev][1] + [root.val]]  
            if p.val not in paths or q.val not in paths:                
                leaves(root.left, root.val)
                leaves(root.right, root.val)     
                
        leaves(root, root.val)            
        pathP, pathQ = paths[p.val][1],paths[q.val][1]

        length = min(len(pathP),len(pathQ))
        for i in range(length):
            if pathP[i] != pathQ[i]:
                return paths[pathP[i-1]][0]
        return paths[pathP[length-1]][0]

    
# Sample solution for 64 ms using dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # '''
    # 2 conditions: 
    # 1 - both are ancestors of the same path (L/R): keep going down
    # 2 - both are ancestors of different path (one L one R): return node
    # Plan:
    # - DFS recursively and at each 'split' keep track of if p and/or q are found down left and right
    # - check conditions
    #     - once true from both sides, return the Node itself (current_node)
    # '''
        def dfs(current, p, q):

            ret_val = False
            
            if current == p or current == q: ret_val = True
            
            left, right = False, False
            

            if current.left:
                left = dfs(current.left, p, q)
                if type(left) == TreeNode: 
                    return left
                elif ret_val and left:
                    return current

                
            if current.right:
                right = dfs(current.right, p, q)
                if type(right) == TreeNode: 
                    return right
                elif ret_val and right:
                    return current
            
            if left and right: 
                return current
            elif left or right:
                return True
            else:
                return ret_val
            
        result = dfs(root, p, q)
        return result
