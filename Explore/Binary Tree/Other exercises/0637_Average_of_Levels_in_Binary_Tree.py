# Problem 637
# Date: 2019/09/09

# 56 ms
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        avg = []
        def average(arr):            
            return sum(arr)/len(arr)
        
        def getLevelAvg(arr):
            values = [a.val for a in arr]
            if values:
                avg.append(average(values))
                getLevelAvg([side for a in arr if a for side in (a.left, a.right) if side])
            
        if root: getLevelAvg([root])   
            
        return avg
