# Problem 1261
# Date completed: 2019/11/21 

# 132 ms (11%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        
        queue = [root]
        self.max = 0
        def setNode(node,val):
            if node: 
                node.val = val
                queue.append(node)
                self.max = max(self.max,val)
                
        while queue:
            node = queue.pop(0)
            setNode(node.left, 2*node.val+1)
            setNode(node.right, 2*node.val+2)   
            
        self.root = root

    
    def find(self, target: int) -> bool:

        if target > self.max: return False
        
        isLeftArr = []
        while target>0:
            isLeftArr.append(target%2==1)
            target = (target-1)//2
        
        node = self.root
        while isLeftArr:
            isLeft = isLeftArr.pop()
            if (isLeft and node.left) or ((not isLeft) and node.right):
                node = node.left if isLeft else node.right
            else:
                return False
        
        return True

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
