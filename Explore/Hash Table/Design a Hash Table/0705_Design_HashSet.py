# Problem 705 
# Date completed: 2019/09/20

# 184 ms
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.N = 1000
        self.data = [[] for i in range(self.N)]


    def add(self, key: int) -> None:
        n = key%self.N
        if key not in self.data[n]:
            self.data[n].append(key)

    def remove(self, key: int) -> None:
        try:
            n = key%self.N
            self.data[n].pop(self.data[n].index(key))
        except:
            return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.data[key%self.N]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
