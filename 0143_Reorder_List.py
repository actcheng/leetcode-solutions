# Problem 143
# Date completed: 2020/08/20

# 88 ms (96%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next: return
        
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        
        # Reverse list
        nex, slow.next = slow.next, None
        while nex:
            nex.next, slow, nex = slow, nex, nex.next
        
        node1 = head
        node2 = slow
        while node1 and node2 and node1.next:
            node1.next, node1 = node2, node1.next
            node2.next, node2 = node1, node2.next
        
        if node1: node1.next = node2

