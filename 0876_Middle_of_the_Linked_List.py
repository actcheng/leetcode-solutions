# Problem 876
# Date completed: 2019/11/25 

# 28 ms (91%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast.next:
            slow = slow.next
            fast = fast.next.next or fast.next
            
        return slow
