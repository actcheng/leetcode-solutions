# Problem 338
# Date completed: 2019/09/07

# 100 ms

class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]        
        if num >=1 : ans.append(1)
        if num >=2 : ans.append(1)
        store = ans.copy()
        i = 3
        j = 4
        while i <= num:
            if j >= len(store)-1:
                ans.append(ans[-1]+1)
                store = ans.copy()
                j = -1
            else:
                # print(len(store), j, store[j])
                ans.append(store[j]+1)
                # print(ans)
            i += 1
            j += 1
        return ans
