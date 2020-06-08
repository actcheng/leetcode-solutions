# Problem 528
# Date completed: 2020/06/05 

# 252 ms (69%)

class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        self.w = [d/total for d in w]
        self.len = len(self.w)
        for i in range(self.len-1):
            self.w[i+1] += self.w[i]

    def pickIndex(self) -> int:
        num = random.random()
        # Find the index where self.w[i] >= num > self.w[i-1]
        l, r = 0, self.len - 1
        while l+1 < r:
            mid = (l+r) // 2
            
            if self.w[mid] >= num:
                r = mid
            else:
                l = mid

        return l if self.w[l] >= num else r


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
