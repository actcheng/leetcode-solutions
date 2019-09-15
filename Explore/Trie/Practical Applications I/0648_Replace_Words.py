# Problem 648
# Date: 2019/09/15

# 116 ms
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        
        class Trie:
            def __init__(self):
                self.root = {'*':False}
                
            def insert(self,word):
                node = self.root
                for c in word:
                    if c not in node: node[c] = Trie()
                    node = node[c].root
                node['*'] = True
            
            def replacePrefix(self,word):
                node = self.root
                prefix = []
                for c in word:
                    if c in node:
                        prefix.append(c)                        
                        node = node[c].root
                        if node['*']: break
                    else:
                        break
                
                if node['*']:
                    return ''.join(prefix)
                else:
                    return word
         
        trie = Trie()
        [trie.insert(word) for word in dict]
        return ' '.join([trie.replacePrefix(word) for word in sentence.split()])
