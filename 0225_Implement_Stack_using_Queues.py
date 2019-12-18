# Problem 225
# Date completed: 2019/12/18 

# 28 ms (78%)
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Available operations for queues:
        # top: self.queue[0]
        # pop(0)
        # append
        # empty

        self.queue = [] 
        
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        l = len(self.queue)
        self.queue.append(x)
        for i in range(l):
            self.queue.append(self.queue.pop(0))
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

            
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
