# Problem 0707 
# Date completed: 2019/09/30

# 776 ms
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.prev = None
        self.next = None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index == 0: 
            # print('Return for get', self.val, '(between',self.prev and self.prev.val,'and',self.next and self.next.val,')')
            if self.val != None:
                return self.val
            else:
                return -1
        if self.next:
            # print('Get after',self.val,index, '(between',self.prev and self.prev.val,'and',self.next and self.next.val,')')
            return self.next.get(index-1)
        else: 
            return -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new = MyLinkedList()
        new.val = self.val
        new.prev = self
        new.next = self.next
        
        if self.next: self.next.prev = new
        self.next = new
        self.val = val

        # print('Add head:', self.val, '(between',self.prev and self.prev.val,'and',self.next and self.next.val,')')

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        # print('Search tail at',self.val, '(between',self.prev and self.prev.val,'and',self.next and self.next.val,')')
        if self.next:
            # print('Search tail after', self.val, '(between',self.prev and self.prev.val,'and',self.next and self.next.val,')')
            self.next.addAtTail(val)
        else:            
            self.val = val
            self.next = MyLinkedList()
            self.next.prev = self     
            # print('Add tail:',self.val,'after',self.prev.val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index <= 0:      
            self.addAtHead(val)      
            # print('Add new node', self.val,'between', self.prev and self.prev.val,'and',self.next and self.next.val)
        elif self.next:
            # print('Search for add after',self.val,index)
            self.next.addAtIndex(index-1,val)
        # else:
        #     print(val,' is not added')
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            # print('Delete', self and self.val,'between',self.prev and self.prev.val,'and',self.next and self.next.val)   
            if not self.prev: 
                print('Delete first node')
                self.val = self.next and self.next.val
                self.next = self.next and self.next.next
                if self.next: self.next.prev = self
            elif self.next:
                self.prev.next = self.next
                if self.next: self.next.prev = self.prev
                # print(self.next and self.next.prev and self.next.prev.val,'(',self.prev.val,')''is connected to',self.prev and self.prev.next and self.prev.next.val)
        elif self.next:
            # print('Search for delete after', self.val, '(between',self.prev and self.prev.val,'and',self.next and self.next.val,')')
            self.next.deleteAtIndex(index-1)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
