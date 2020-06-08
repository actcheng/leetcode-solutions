# Problem 518
# Date completed: 2020/06/08 

# 488 ms (32%)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        if not coins: return 0
        coins.sort()
        store = {}
        def helper(target,num):
            if (target, num) in store: return store[(target,num)]
            res = 0
            for key in coins:
                if key > target or key > num: break
                res += 1 if key == target else helper(target-key,key)

            store[(target,num)] = res
            return res
        
        return helper(amount,max(coins))
