# Problem 744
# Date completed: 2019/10/05 

# 120 ms (93%)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,r = 0, len(letters)
        while l<r:
            mid = (l+r)//2
            if letters[mid] <= target:
                l = mid+1
            else:
                r = mid
        
        return letters[r] if r < len(letters) else letters[0]
