# Problem 234
# Date completed: 2019/11/19 

# 80 ms (54%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        slow = head
        fast = head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next            
            fast = fast.next.next
            
        if fast: slow = slow.next
        
        while slow:
            val = stack.pop()
            if val != slow.val: return False
            slow = slow.next
            
        return True
        
