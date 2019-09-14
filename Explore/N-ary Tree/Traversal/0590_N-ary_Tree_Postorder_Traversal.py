# Problem 590 
# Date: 2019/09/14

# 672 ms
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.arr = []
        
        def transverse(root):
            if not root: return
            [transverse(c) for c in root.children]
            self.arr.append(root.val)
            return
        
        transverse(root)
        return self.arr
