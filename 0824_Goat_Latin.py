# Problem 824
# Date completed: 2020/08/19

# 44 ms (23%)
class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.strip().split(' ')
        vowels = set(['a','e','o','i','u'])
        for i in range(len(words)):
            if words[i][0].lower() not in vowels:
                words[i] = words[i][1:] + words[i][0]
                
            words[i] += 'ma' + 'a'*(i+1)            
            
        return ' '.join(words)
