# Problem 524
# Date completed: 2020/01/13 

# 676 ms (29%)
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def generate(word):
            i = 0
            j = 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i+=1
            
            return j == len(word)
                
                
        s_counts = collections.Counter(s)
        keys = set(s_counts.keys())
        longest = ''
        for word in d:
            # Conditions to skip without count:
            # - word is longer than s
            # - word contains letters not in s
            if (len(word) >= len(longest) and  
                ((not len(word) == len(longest)) or longest>word)and
                len(word) <= len(s)):
                if generate(word): 
                    longest = word if not longest or len(word)>len(longest) else min(longest,word)
            
        return longest
