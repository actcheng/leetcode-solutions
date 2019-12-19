# Problem 133
# Date completed: 2019/12/19 

# 36 ms (88%)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # If not node, return None
        # Create the first node with value of the given node
        # For each neighbor of the given node:
        #  1. create a new node with the value
        #  2. add the node as neighbor of the copied node
        #  3. push the new node and the corresponding original node into a queue
        # Iterate over the queue, repeat 1-3 if a neighbor in the original node does not present in the new node
        
        if not node: return None
        
        node_new = Node(node.val,[]) # This is the node to be returned

        queue = [node]
        nodes = {node: node_new}
        while queue:
            orig = queue.pop(0)
            new = nodes[orig]
            
            for neighbor in orig.neighbors:
                if neighbor not in nodes:
                    neighbor_new = Node(neighbor.val,[])                    
                    queue.append(neighbor)
                    nodes[neighbor] = neighbor_new
                new.neighbors.append(nodes[neighbor])
                    
        return node_new
