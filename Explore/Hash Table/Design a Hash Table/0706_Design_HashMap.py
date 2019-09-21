# Problem 706 
# Date completed: 2019/09/20

# 232 ms
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.N = 1000
        self.key = [[] for i in range(self.N)]
        self.value = [[] for i in range(self.N)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        n = key%self.N
        if key in self.key[n]:
            self.value[n][self.key[n].index(key)] = value
        else:
            self.key[n].append(key)
            self.value[n].append(value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        n = key%self.N
        if key in self.key[n]:
            return self.value[n][self.key[n].index(key)]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        n = key%self.N
        if key in self.key[n]:
            ind = self.key[n].index(key)
            self.key[n].pop(ind)
            self.value[n].pop(ind)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
