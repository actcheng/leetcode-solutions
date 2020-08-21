# Problem 82
# Date completed: 2020/08/21 

# 44 ms (67%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
    
        cur = head.val
        dup = head.val == head.next.val
        while dup:
            while head and head.val == cur: head = head.next
            if not head or not head.next: return head
            
            cur = head.val
            dup = head.val == head.next.val
            
        head.next = self.deleteDuplicates(head.next)
            
        return head
                
            
