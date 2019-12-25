# Problem 476
# Date completed: 2019/12/25

# 20 ms (98%)
class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join('0' if b=='1' else '1' for b in bin(num).split('b')[-1]),2)
