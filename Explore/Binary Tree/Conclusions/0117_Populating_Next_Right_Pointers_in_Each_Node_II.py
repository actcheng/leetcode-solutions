# Problem 117
# Date: 2019/09/08

# Referenced from discuss
# 428 ms
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        prevNode = None
        nextLevLeft = None
        
        while node:
            if node.left:
                if prevNode: 
                    prevNode.next = node.left
                    # print('{}->{}'.format(prevNode.val,prevNode.next.val))
                prevNode = node.left
                if not nextLevLeft: nextLevLeft = node.left
            
            if node.right:
                if prevNode: 
                    prevNode.next = node.right
                    # print('{}->{}'.format(prevNode.val,prevNode.next.val))
                prevNode = node.right
                if not nextLevLeft: nextLevLeft = node.right
            
            if node.next:
                node = node.next
            else:
                node = nextLevLeft
                prevNode = None
                nextLevLeft = None
                
        return root
