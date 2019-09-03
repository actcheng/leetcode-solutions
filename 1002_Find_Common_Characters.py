# Problem 1002
# Date completed: 2019/09/03

# 56 ms
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        arr = []
        quit = False
        for c in A[-1]:
            if c in A[-1]:
                common = True
                print('j')
                for j in range(len(A)-1):
                    ind = A[j].find(c)
                    if ind == -1:
                        common = False
                        break
                    elif len(A[j]) > 1:
                        A[j] = A[j][:ind] + A[j][ind+1:]
                    else:
                        quit = True
                if common: 
                    arr.append(c)
                else: 
                    A[-1] = A[-1].replace(c,'')
                if quit: break
        return arr
