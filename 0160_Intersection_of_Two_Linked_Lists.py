# Problem 160
# Date completed: 2019/12/18 

# 168 ms (58%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        # get length
        def getLen(head):
            l = 0
            node = head
            while node: 
                node = node.next
                l += 1
                
            return l
        
        def forwardSteps(head,steps):
            for i in range(steps):
                head = head.next
            return head
        
        l_A, l_B = getLen(headA), getLen(headB)
        if l_A > l_B: headA = forwardSteps(headA,l_A-l_B)
        if l_B > l_A: headB = forwardSteps(headB,l_B-l_A)
            
        while headA:
            if headA==headB: return headA
            headA = headA.next
            headB = headB.next
            
        return None
