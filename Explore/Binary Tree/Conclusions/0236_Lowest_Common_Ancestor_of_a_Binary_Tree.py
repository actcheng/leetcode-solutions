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
