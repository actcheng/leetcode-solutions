# Problem 133
# Date completed: 2019/10/25 

# 44 ms (81%)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None               
        checked = {node:Node(node.val,[])}
        stack = [node]
        while stack:
            old = stack.pop()
            for neighbor in old.neighbors:
                if neighbor not in checked:
                    checked[neighbor] = Node(neighbor.val,[])
                    stack.append(neighbor)
                checked[old].neighbors.append(checked[neighbor])               
        
        return checked[node]
