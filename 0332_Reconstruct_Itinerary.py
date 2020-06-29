# Problem 332
# Date completed: 2020/06/28

# 72 ms, 98%
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        routes = collections.defaultdict(list)
        for dep, arr in tickets:
            routes[dep].append(arr)
            
        for dep in routes:
            routes[dep].sort(reverse=True)
        
        itin = []
        stack = ["JFK"]
        while stack:
            cur = stack[-1]
            if len(routes[cur]) > 0:
                stack.append(routes[cur].pop())
            else:
                itin.insert(0,stack.pop())
            
        return itin
