# Problem 303
# Date completed: 2019/12/19 

# 80 ms (89%)
class NumArray:

    def __init__(self, nums: List[int]):
        self.accum = list(nums)
        for i in range(1,len(nums)):
            self.accum[i] += self.accum[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.accum[j] - self.accum[i-1] if i>0 else self.accum[j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
