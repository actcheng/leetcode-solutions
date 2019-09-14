# Problem 208 
# Date: 2019/09/14

# 200 ms
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.isWord = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self
        for c in word:
            if c not in root.children:
                root.children[c] = Trie()
            root = root.children[c]   
        root.isWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self
        for c in word:
            if c not in root.children: return False
            root = root.children[c]
        return root.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self
        for c in prefix:
            if c not in root.children: return False
            root = root.children[c]        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
