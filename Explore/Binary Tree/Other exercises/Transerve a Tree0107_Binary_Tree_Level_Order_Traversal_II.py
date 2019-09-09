# Problem 107
# Date: 2019/09/09

# 40 ms
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return None
        ans = collections.deque()
        def getNextLevel(inArr):
            # print([a.val for a in inArr if a])
            thisLevel = []
            nextLevel = []
            while inArr:
                node = inArr.pop(0)
                if node:
                    thisLevel.append(node.val)
                    nextLevel.append(node.left)
                    nextLevel.append(node.right) 
            
            if thisLevel: ans.appendleft(thisLevel)             
            if nextLevel: getNextLevel(nextLevel) 
                
            return 
        
        getNextLevel([root])
        
        return ans
