# Problem 203
# Date completed: 2019/12/18 

# 64 ms (92%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        
        node = head
        while node:
            while node.next and node.next.val == val:
                node.next = node.next.next
            node = node.next
        
        return head
