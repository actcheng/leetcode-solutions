# Problem 116
# Date: 2019/09/06

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def pointRight(left, right):
            
            if left and right:
                pointRight(left.left,left.right)
                pointRight(left.right,right.left)                
                pointRight(right.left,right.right)  
                pointRight(right.right,None)
                left.next = right
                
            elif left: 
                pointRight(left.left,left.right)
                left.next = None
                

        pointRight(root,None)
        return root
