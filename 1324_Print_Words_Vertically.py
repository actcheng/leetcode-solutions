# Problem 1324
# Date completed: 2020/01/19 

# 24 ms (100%)
class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split()
        max_len = max(len(text) for text in arr)
        
        n_rows = []
        for i in range(max_len):
            n_rows.append(len(arr) if i==0 else n_rows[i-1])
            while len(arr[n_rows[-1]-1]) < (i+1):
                n_rows[-1] -= 1

        return ["".join([arr[j][i] if i<len(arr[j]) else " " for j in range(n_rows[i])]) for i in range(max_len)]
