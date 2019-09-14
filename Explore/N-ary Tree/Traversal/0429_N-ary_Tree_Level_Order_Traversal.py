# Problem 429
# Date: 2019/09/14

# 680 ms
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:        
        def helper(nodes,arr):
            if nodes:
                arr.append([node.val for node in nodes])
                helper([child for node in nodes for child in node.children],arr)
                
        arr = []
        if root: helper([root],arr)
        return arr
