# Problem 19
# Date completed: 2019/11/18 

# 24 ms (99%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        
        if not fast: 
            return slow.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        if slow.next: slow.next = slow.next.next
        return head
