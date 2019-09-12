# Problem 412
# Date completed: 2019/09/12

# 56 ms

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(n):
            numStr = ''
            if (i+1) % 3 == 0: numStr += 'Fizz'
            if (i+1) % 5 == 0: numStr += 'Buzz'
            arr.append(numStr or str(i+1))
            
        return arr
