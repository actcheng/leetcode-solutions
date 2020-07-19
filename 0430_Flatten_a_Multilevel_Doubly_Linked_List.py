# Problem 430
# Date completed: 2020/07/10

# 52 ms (41%)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
            
        def helper(node):            
            while node:
                if node.child:
                    child_head = node.child
                    child_tail = helper(node.child)                    
                    
                    child_tail.next = node.next
                    if node.next: child_tail.next.prev = child_tail
                    
                    node.next = child_head
                    child_head.prev = node
                    node.child = None
                    
                    node = child_tail
                    
                if node.next is not None:             
                    node = node.next
                else:
                    break
                
            return node
        
        tail = helper(head)
        
        return head
        
