# Problem 211 
# Date: 2019/09/15

# 356 ms
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {'*':False}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            if c not in node: node[c]=WordDictionary()
            node = node[c].root
        node['*'] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        if not word: return node['*']
        
        
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for key in node:
                    if key != '*': 
                        found = node[key].search(word[i+1:])                    
                        if found: return True
                return False
                        
            else:
                if c in node:
                    node = node[c].root
                else:
                    return False     
                
        return node['*']
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
