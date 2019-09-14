# Problem 108 
# Date: 2019/09/14

# 80 ms
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        if nums == []: return None
        ind = int(len(nums)/2)
        
        root = TreeNode(nums[ind])
        root.left = self.sortedArrayToBST(nums[:ind])
        if ind+1 < len(nums): root.right = self.sortedArrayToBST(nums[ind+1:])
        
        return root
