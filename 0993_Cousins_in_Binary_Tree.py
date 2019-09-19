# Problem 993 
# Date completed: 2019/09/19

# 32 ms
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        if not root or root.val == x or root.val == y: return False
        
        self.found = None # [parent value, depth]
        
        def dfs(node,depth,parentVal):
            if not node: return False
            # print('Search', node.val)
            if node.val == x or node.val == y:
                if not self.found:
                    self.found = [parentVal,depth]
                    # print('Found!',self.found,node.val)
                else:
                    # print('Found!',self.found,[parentVal,depth],node.val)
                    if parentVal != self.found[0] and depth == self.found[1]:
                        return True
                    else:
                        return False
            else:
                return dfs(node.left,depth+1,node.val) or dfs(node.right,depth+1,node.val)
                 
        return dfs(root,0,'None')  
            
