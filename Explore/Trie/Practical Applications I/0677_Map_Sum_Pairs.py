# Problem 667
# Date: 2019/09/14

# 32 ms
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {'*':0}

    def insert(self, key: str, val: int) -> None:
        root = self.root
        for c in key:
            if c not in root:
                root[c] = MapSum()
            root = root[c].root        
        root['*'] = val

    def sum(self, prefix: str) -> int:
        
        root = self.root
        for c in prefix:
            if c not in root: return 0
            root = root[c].root
        
        total = root['*']
        queue = [root]
        while queue:
            root = queue.pop(0)
            # print(root)
            for key in root:
                if key != '*':
                    total += root[key].root['*']
                    queue.append(root[key].root)
        return total

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
