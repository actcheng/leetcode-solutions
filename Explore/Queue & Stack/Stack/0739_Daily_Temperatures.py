# Problem 739
# Date completed: 2019/10/20 

# 620 ms (17%)
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = []
        stack = []
        for i in range(len(T)-1,-1,-1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            if stack:
                res.append(stack[-1]-i)
            else:
                res.append(0)
            stack.append(i)
        res.reverse()
        return res
