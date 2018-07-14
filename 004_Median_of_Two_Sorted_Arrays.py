# Problem #4
# Date completed: 2018/07/04

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1=len(nums1)
        l2=len(nums2)
        l=[]
        while nums1 and nums2:
            if nums1[0]<nums2[0]:
                l.append(nums1.pop(0))
            else:
                l.append(nums2.pop(0))
        l=l+nums1+nums2
        
        mid=(l1+l2)//2
        res=(l1+l2)%2
        
        if res>0:
            a=l[mid]
        else:
            a=(l[mid]+l[mid-1])/2
            
        return a
