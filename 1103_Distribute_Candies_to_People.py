# Problem 1103
# Date completed: 2020/08/18

# 28 ms (93%)
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        res = [0 for _ in range(num_people)]
        
        give = 1
        i = 0
        while candies > give:
            res[i] += give
            candies -= give
            give += 1
            i += 1
            if i == num_people: i = 0

        res[i] += candies
        
        return res
