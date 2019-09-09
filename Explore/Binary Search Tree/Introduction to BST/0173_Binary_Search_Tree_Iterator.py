# Problem 173
# Date: 2019/09/09

# 176 ms
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.pointer = []
        node = root
        while node:            
            self.pointer.append([node, False])
            node = node.left
        print([[n.val, ret] for [n,ret] in self.pointer])
            
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.pointer: return None
        root, returned = self.pointer.pop()              
        
        if root.right:
            self.pointer.append([root, True])
            node = root.right
            while node:
                self.pointer.append([node, False])
                node = node.left
                
        nextVal = root.val
        while self.pointer and self.pointer[-1][1]:
            self.pointer.pop()
            
        print([[n.val, ret] for [n,ret] in self.pointer])
        return nextVal
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.pointer) > 0

# 88 ms
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.pointer = []
        node = root
        while node:            
            self.pointer.append(node)
            node = node.left
        # print([n.val for n in self.pointer])
            
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.pointer: return None
        root= self.pointer.pop()              
        
        if root.right:
            node = root.right
            while node:
                self.pointer.append(node)
                node = node.left
                
        nextVal = root.val
            
        # print([n.val for n,ret in self.pointer])
        return nextVal
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.pointer) > 0
