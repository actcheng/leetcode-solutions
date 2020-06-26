# Problem 787
# Date completed: 2020/06/14 

# 120 ms, 57%
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst: return 0
        
        store = collections.defaultdict(list)

        for u, v, w in flights:
            store[u].append((v,w)) 
            
        price = {u:float('inf') for u in range(n)}
        
        if src not in store: return -1        
        
        queue = [(src,0,0)]

        while queue:
            u, cost, k = queue.pop(0)
            for v, w in store[u]:
                if cost+w < price[v]:
                    price[v] = cost+w
                    if v != dst and k < K:
                        queue.append((v,cost+w,k+1))
                    
        return price[dst] if price[dst] != float('inf') else -1
