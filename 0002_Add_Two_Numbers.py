# Problem #2
# Date completed: 2018/07/04

# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
#    def addNode()

class Solution:       
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        node=[]
        num = l1.val+l2.val
        carry = num>9
        num -=carry*10
        node.append(ListNode(num))

        n=0
        while l1.next!=None and l2.next!=None:            
            l1 = l1.next
            l2 = l2.next
            num = l1.val+l2.val+carry
            carry = num>9
            num-= carry*10
            node.append(ListNode(num))
            node[n].next=node[n+1]
            n+=1        
            
        if l1.next==None and l2.next==None and carry==1:
            node.append(ListNode(1))
            node[n].next=node[n+1]
        else:
            while l1.next!=None:
                l1 = l1.next
                num = l1.val+carry
                carry = num>9
                num-= carry*10
                node.append(ListNode(num))
                node[n].next=node[n+1]
                n+=1
                
            while l2.next!=None:
                l2 = l2.next
                num = l2.val+carry
                carry = num>9
                num-= carry*10
                node.append(ListNode(num))
                node[n].next=node[n+1]
                n+=1
        if carry == 1:
            node.append(ListNode(1))
            node[n].next=node[n+1]                       
            
        return node[0]
