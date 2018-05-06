# 这道题一开始错了，错误的原因在于整数的除法取整需要使用//来除
# 还有就是从0开始的序号得注意下
# python 的sort不知道算不算作弊2333

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3.sort()

        len3 = len(nums3)
        if len3%2 != 0:
            return float(nums3[len3//2])
        else:
            return float(nums3[len3//2] + nums3[len3//2-1])

