# Problem 500
# Date completed: 2019/11/08 

# 24 ms (99%)
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set(list('qwertyuiop')),
                set(list('asdfghjkl')),
                set(list('zxcvbnm'))]
        res = []
        for word in words:
            word_set = set(list(word.lower()))
            if any([word_set.issubset(row) for row in rows]):
                res.append(word)
        return res
