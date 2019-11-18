# Problem 919
# Date completed: 2019/11/18 

# 60 ms (93%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.thisLevel = []
        self.nextLevel = []
        self.depth = None
        
        self.dfs(root,0)
        
        if not self.thisLevel: 
            self.thisLevel, self.nextLevel = self.nextLevel, []
            
    def dfs(self,node,depth):

        if not node.left and not node.right:
            if not self.depth: self.depth = depth
        
        def appendLevel(node,depth):
            if depth < self.depth:
                self.thisLevel.append(node)
            else:
                self.nextLevel.append(node)
                
        if node.left:
            self.dfs(node.left,depth+1)
        else:
            appendLevel(node,depth)

        if node.right:
            self.dfs(node.right,depth+1)
        else:
            appendLevel(node,depth)
                
    def insert(self, v: int) -> int:
        node = self.thisLevel.pop(0)
        new_node = TreeNode(v)
        if not node.left: 
            node.left = new_node 
        else:
            node.right = new_node 
        
        self.nextLevel.append(new_node)
        self.nextLevel.append(new_node)
        
        if not self.thisLevel: 
            self.thisLevel, self.nextLevel = self.nextLevel, []
            
        return node.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
