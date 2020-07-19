# Problem 957
# Date completed: 2020/07/06 

# 124 ms
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        
        code = ''.join([str(i) for i in cells])
        store = [code]

        for i in range(N):
            code = '0'
            for j in range(1,7):
                code += '1' if store[-1][j-1] == store[-1][j+1] else '0'
            code += '0'
            
            if code in store: 
                if store.index(code) != 0: 
                    store.pop(0)
                    N -= 1
                    
                return [int(i) for i in store[N%(len(store))]]
                      
            store.append(code)
        
        return [int(i) for i in store[-1]]

