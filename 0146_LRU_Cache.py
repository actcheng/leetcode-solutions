# Problem 146
# Date completed: 2020/04/24 

# 924 ms (8.7%)
class LRUCache:

    def __init__(self, capacity: int):
        
        self._store = {} # key: [value, history]
        self._capacity = capacity
        self._history = [] # Do it in a slow way, anyway
        self._counter = 0
        
    def get(self, key: int) -> int:        
        if key in self._store:
            self._counter += 1
            # Update priority of key
            self._store[key][1] = self._counter
            # print('get ', key, 'new counter ', self._counter)
            return self._store[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if key in self._store: return
        
        # print(self._store, len(self._store), self._capacity)
        if key not in self._store and len(self._store) == self._capacity:
            # print('reached capacity!')
            # Invalidate least used element            
            del self._store[self.find_min_key()]            
        
        self._counter += 1
        self._store[key] = [value, self._counter]
        # print('new counter ', self._counter)
        # print(self._store)

    def find_min_key(self):
        min_key = None
        min_val = None
        for key in self._store:
            if not min_val or self._store[key][1] < min_val:
                min_key = key
                min_val = self._store[key][1]
                
        # print('Min key = ', min_key)
        return min_key
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Sample solution (168 ms)
from collections import defaultdict
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = defaultdict(int)
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            val = self.dic[key]
            self.put(key, val)
            return val
        
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            del self.dic[key]
            self.dic[key] = value
            return
        
        self.dic[key] = value
        if len(self.dic) > self.capacity:
            del self.dic[next(iter(self.dic))]
            # print(self.dic)
            
