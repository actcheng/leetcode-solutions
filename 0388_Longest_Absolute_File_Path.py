# Problem 388
# Date completed: 2019/11/11 

# 28 ms (96%)
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        arr = input.split('\n')
        longest = 0
        stack = []
        level = 0
        while arr:
            a = arr.pop(0)
            split = a.split('\t')
            nt = len(split)-1 
            name = split[-1]          
            stack = stack[:nt]
            stack.append(name)
            if '.' in name:
                longest = max(longest, len('/'.join(stack)))
                # print('/'.join(stack))
        return longest
