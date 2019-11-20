# Problem 1019
# Date completed: 2019/11/20 

# 332 ms (98%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head: return []
        if not head.next: return [0]
        i = 0
        res = [0]
        store = [[head.val,0]]
        node = head.next
        while node:
            res.append(0)
            i += 1
            while store and node.val > store[-1][0]:
                val, loc = store.pop()
                res[loc] = node.val   
            store.append([node.val,i])
            node = node.next
            
        return res
