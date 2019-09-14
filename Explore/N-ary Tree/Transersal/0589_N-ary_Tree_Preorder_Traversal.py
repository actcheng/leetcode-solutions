# Problem 589 
# Date: 2019/09/14

# 663 ms
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.arr = []
        
        def transverse(root):
            if not root: return
            self.arr.append(root.val)
            for c in root.children:
                transverse(c)
        
        transverse(root)
        return self.arr
