# Problem 21 
# Date completed: 2019/09/14

# 40 ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:        
        
        def mergeNext(head, l1Node, l2Node):
            if not (l1Node or l2Node): return
            if not l1Node: 
                head.next = l2Node
                return
            if not l2Node: 
                head.next = l1Node
                return
                
            if l1Node.val > l2Node.val:
                head.next = l2Node
                mergeNext(l2Node,l1Node,l2Node.next)
            else: 
                head.next = l1Node
                mergeNext(l1Node,l1Node.next,l2Node)

        head = ListNode(0)
        mergeNext(head,l1,l2)
        
        return head.next
