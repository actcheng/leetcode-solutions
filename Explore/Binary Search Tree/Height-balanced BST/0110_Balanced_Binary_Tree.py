# Problem 110
# Date: 2019/09/14

# 64 ms
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def findDepth(node):
            
            if not node: return 1
            if not (node.left or node.right):
                print(node.val,1)
                return 2
            else:
                leftDepth = findDepth(node.left)
                rightDepth = findDepth(node.right)
                if (not (leftDepth and rightDepth) or
                    abs(leftDepth-rightDepth)>1): 
                    # print(node.val,leftDepth,rightDepth)
                    return False
                else:
                    # print(node.val, max(leftDepth,rightDepth) + 1)
                    return max(leftDepth,rightDepth) + 1
        
        # if not root: return True
        
        depth = findDepth(root)
        
        if depth: 
            return True
        else:
            return False
                
