# Problem 24
# Date completed: 2019/11/05 

# 36 ms (78%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head        
        head, head.next, head.next.next = head.next, head, self.swapPairs(head.next.next)           
        
        return head
