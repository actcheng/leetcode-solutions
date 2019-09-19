# Problem 404 
# Date completed: 2019/09/19

# 52 ms (slow?)
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        sum = 0
        queue = [root]
        while queue:
            root = queue.pop(0)
            if root.left:
                if not (root.left.left or root.left.right):
                    sum += root.left.val
                    print(root.left.val,sum)
                else:
                    queue.append(root.left)
            if root.right: queue.append(root.right)
                
        return sum
