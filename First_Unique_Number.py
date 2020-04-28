# Date completed: 2020/04/28 

# 752 ms 

class FirstUnique:

    def __init__(self, nums: List[int]):
        
        counts = collections.Counter(nums)
        
        self._unique = collections.OrderedDict()
        for num in counts:
            if counts[num] == 1:
                self._unique[num] = 1
                
        self._all = set(counts.keys())
        
    def showFirstUnique(self) -> int:
        if self._unique:
            for num in self._unique:
                return num
        return -1

    def add(self, value: int) -> None:
        
        if value not in self._all: # New unique value
            self._all.add(value)
            self._unique[value] = 1
        elif value in self._unique: # value may appear once
            del self._unique[value]   
            
        
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
