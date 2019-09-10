# Problem 958
# Date: 2019/09/10

# 44 ms
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root: return True
        
        # 1. Check if this level is full 
        # 2. If full, check next level
        # 3. If not full,
        #     (a) check if there are gaps
        #     (b) check if next level exist -> False

        def helper(queue, gap = False):    
            # print(len(queue), gap)
            newQueue = []
            while queue:
                node = queue.pop(0)
                
                if gap and (node.left or node.right): return False
                
                if node.left:
                    newQueue.append(node.left)
                    if node.right: 
                        newQueue.append(node.right)
                    else:
                        gap = True
                else:
                    if node.right: return False
                    gap = True
                    
                    
                # print('newQueue', len(newQueue))
                
            return len(newQueue) == 0 or helper(newQueue,gap)
        
        return helper([root])
 
            
