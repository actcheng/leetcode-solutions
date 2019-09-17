# Problem 88 
# Date completed: 2019/09/17

# 44 ms
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m-1, n-1, m+n-1
        while i>=0 and j>=0:
            if nums1[i]>=nums2[j]:
                nums1[k]=nums1[i]
                nums1[i]=0
                i -= 1
            else:
                nums1[k]=nums2[j]
                j -= 1
            k-=1
            # print(i,j,k,nums1,nums2)
        if j>=0: nums1[:j+1] = nums2[:j+1]
            
