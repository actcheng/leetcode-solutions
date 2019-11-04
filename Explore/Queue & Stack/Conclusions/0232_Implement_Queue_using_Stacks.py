# Problem 232
# Date completed: 2019/11/04 

# 32 ms (91%)
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.stack2 = [] # Reverse of self.stack
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.front == None: self.front = x
        if self.stack2 != []:
            while self.stack2:
                self.stack.append(self.stack2.pop())
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack2 == []:
            while self.stack:
                self.stack2.append(self.stack.pop())
                
        res = self.stack2.pop()    
        self.front = self.stack2[-1] if len(self.stack2) > 0 else None
        return res
    
    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) + len(self.stack2) == 0 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
