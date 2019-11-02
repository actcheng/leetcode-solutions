# Problem 125
# Date completed: 2019/11/02

# 64 ms (39%)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [x.lower() for x in s if x.isalpha() or x.isnumeric()]
        return all(a==b for a,b in zip(arr[:len(arr)//2],arr[:len(arr)//2-1+len(arr)%2:-1]))
