# Problem 328
# Date completed: 2020/05/17 

# 88 ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        odd_head, odd_tail = head, head
        even_head, even_tail = head.next, head.next
        
        while even_tail and even_tail.next:
            odd_tail.next, even_tail.next = even_tail.next, even_tail.next.next
            odd_tail, even_tail = odd_tail.next, even_tail.next
            
        odd_tail.next = even_head
        
        return odd_head
        

