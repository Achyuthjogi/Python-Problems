#Platform: Leetcode
#Problem: Median of two array
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        comblist = sorted(nums1 + nums2)
        n = len(comblist)
        mid = n // 2
        if n % 2 == 1:
            return comblist[mid]
        else:
            return (comblist[mid-1]+ comblist[mid]) / 2

        
