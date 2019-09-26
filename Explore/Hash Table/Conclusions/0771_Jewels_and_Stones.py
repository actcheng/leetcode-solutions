# Problem 771
# Date completed: 2019/09/26

# 36 ms
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = {x:0 for x in J}
        for x in S:
            if x in jewels: jewels[x] += 1
        return sum(list(jewels.values()))
