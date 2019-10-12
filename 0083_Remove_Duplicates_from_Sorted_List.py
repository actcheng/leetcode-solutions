# Problem 83
# Date completed: 2019/10/12

# 44 ms (91%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        self.unique = set([])
        
        def helper(head,prev):
            if not head: return
            if head.val in self.unique:
                prev.next = head.next
            else:
                self.unique.add(head.val)
                prev = head
            
            if head.next: helper(head.next,prev)
                
        helper(head,head)
        return head


