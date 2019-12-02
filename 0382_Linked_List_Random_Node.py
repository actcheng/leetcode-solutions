# Problem 382
# Date completed: 2019/12/02 

# 72 ms (99%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.arr = []
        node = head
        while node:
            self.arr.append(node.val)
            node = node.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self.arr)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
