# Problem 345
# Date completed: 2019/12/19 

# 52 ms (81%)
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(list('aeiouAEIOU'))
        vow = []
        for i in range(len(s)):
            if s[i] in vowels: vow.append(s[i])
        
        vow = [c for c in s if c in vowels]
        res= [vow.pop() if c in vowels else c for c in s]
        # print(res)
        
        return ''.join(res)
            
