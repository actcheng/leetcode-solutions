# Problem 206
# Date completed: 2019/11/06 

# 32 ms (99%)
# Recursive
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        tail = self.reverseList(head.next)
        head.next.next = head
        head.next = None
       
        return tail    
