# Problem 1286
# Date completed: 2020/08/23

# 64 ms (25%)
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.char = characters
        self.len = len(characters)
        self.combl = combinationLength
        self.path = [i for i in range(self.combl)]
        self.end = False
        
    def next_vacant(self,start):
        for i in range(start+1,self.len):
            if i not in self.path: return i            
        return False
    
    def move_path(self):

        target = self.next_vacant(self.path.pop())
        while not target and self.path:            
            target = self.next_vacant(self.path.pop())
            if target > self.len-self.combl+len(self.path): target = False

        if not target:  
            self.end = True
        else: 
            self.path.append(target)
            while len(self.path) < self.combl:
                target = self.next_vacant(target)
                self.path.append(target)
                
            # print(self.path)
        
    def next(self) -> str:
        res = ''.join(self.char[i] for i in self.path)
        self.move_path()
        return res

    def hasNext(self) -> bool:
        return not self.end
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

