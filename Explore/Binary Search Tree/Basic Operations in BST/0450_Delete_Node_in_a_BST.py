# Problem 450 
# Date: 2019/09/10

# 68 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:       
            
        def replaceNode(nodeToDelete):
            # Case 1: no child -> delete the node
            if not (nodeToDelete.left or nodeToDelete.right):
                # print('Case 1')
                return None
            # Case 2: one child -> use the child to replace
            elif not (nodeToDelete.left and nodeToDelete.right):
                # print('Case 2')
                if nodeToDelete.left:
                    return nodeToDelete.left 
                else:
                    return nodeToDelete.right
                
            # Case 3: two child -> replace with leftmost leave of the right child
            else:
                # print('Case 3')
                rightChild = nodeToDelete.right
                # no left leaves                
                if not (rightChild.left):
                    # print('No left leaves')
                    replacedNode = rightChild
                    replacedNode.left = nodeToDelete.left
                else:
                    parent = rightChild
                    while parent.left:
                        if parent.left.left:
                            parent = parent.left
                        else:
                            replacedNode = parent.left
                            if replacedNode.left or replacedNode.right:
                                parent.left = replaceNode(replacedNode)     
                            else:
                                parent.left = None
                            replacedNode.left = nodeToDelete.left
                            replacedNode.right = nodeToDelete.right                                                             
                            break
                            
            # print('ReplaceNode:', nodeToDelete.val, replacedNode.val)
            return replacedNode
        
        if not root: 
            return root
        
        if root.val == key:
            return replaceNode(root)

        # BFS
        queue = [root]        
        while queue:
            node = queue.pop(0)
            # print(node.val, node.left.val, node.right.val)
            if node.left:
                if node.left.val == key:
                    # print('Left of', node.val)
                    node.left = replaceNode(node.left)
                    break
                else:
                    queue.append(node.left)
            
            if node.right:
                if node.right.val == key:
                    # print('Right of', node.val)
                    node.right = replaceNode(node.right)
                    break
                else:
                    queue.append(node.right)
                    
        return root
