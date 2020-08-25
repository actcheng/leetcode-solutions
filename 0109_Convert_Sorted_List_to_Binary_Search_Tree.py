# Problem 109
# Date completed: 2020/08/24

# 120 ms (98 %)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        if not head.next: return TreeNode(head.val)
        prev, mid, fast = head, head, head
        while fast and fast.next:
            fast = fast.next.next
            prev, mid = mid, mid.next
        
        prev.next = None
        
#         print('mid',mid.val)
#         print('left')
#         node = head
#         while node:
#             print(node.val)
#             node = node.next
            
#         print('right')
#         node = mid.next
#         while node:
#             print(node.val)
#             node = node.next
        
        node = TreeNode(mid.val)

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
