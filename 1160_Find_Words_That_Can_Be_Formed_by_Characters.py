# Problem 1160
# Date completed: 2019/11/24 

# 172 ms (63%)
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counts = collections.Counter(chars)
        length = 0
        for word in words:
            word_counts = collections.Counter(word)
            good = True
            for char in word_counts:
                if word_counts[char] > char_counts[char]:
                    good = False
                    break
            if good: length += len(word)
                    
        return length
