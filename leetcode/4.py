#!/usr/bin/env python3
from math import ceil


class Solution:
    def median(self, nums):
        length = len(nums)
        middle = length//2
        if length % 2 == 1:
            return nums[middle]
        else:
            return (nums[middle - 1] + nums[middle]) / 2.0

    def merge_median(self, element, nums):
        length = len(nums)

        if length%2 == 1:
            index = length//2
            if element <= nums[index-1]:
                return (nums[index-1] + nums[index]) / 2.0
            if element >= nums[index+1]:
                return (nums[index+1] + nums[index]) / 2.0
            return (element + nums[index]) / 2.0
        else:
            index_max = length//2
            index_min = index_max - 1
            if element <= nums[index_min]:
                return nums[index_min]
            if element >= nums[index_max]:
                return nums[index_max]
            return element

    def merge_median_2(self, a, b, nums):
        length = len(nums)
        index = length/2
        if b <= nums[index - 1]:
            return (max(b,nums[index-2]) + nums[index - 1]) / 2.0
        if a >= nums[index]:
            return (nums[index] + min(a, nums[index + 1])) / 2.0
        return (max(a, nums[index-1]) + min(b, nums[index])) / 2.0


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        >>> solution = Solution()
        >>> solution.findMedianSortedArrays([1, 3], [2])
        2
        """
        while True:
            len1 = len(nums1)
            len2 = len(nums2)

            # The first two are useful only in the first loop
            if len1 == 0:
                return self.median(nums2)
            if len2 == 0:
                return self.median(nums1)
            if len1 == 1 and len2 == 1:
                return (nums1[0] + nums2[0]) / 2.0
            if len1 == 1:
                return self.merge_median(nums1[0], nums2)
            if len2 == 1:
                return self.merge_median(nums2[0], nums1)
            if len1 == 2 and len2 == 2:
                return (max(nums1[0], nums2[0]) + min(nums1[1], nums2[1]))/2.0
            if len1 == 2 and len2%2 == 0:
                return self.merge_median_2(nums1[0], nums1[1], nums2)
            if len2 == 2 and len1%2 == 0:
                return self.merge_median_2(nums2[0], nums2[1], nums1)

            step1 = max(int(ceil(len1/2.0)) - 1, 1)
            step2 = max(int(ceil(len2/2.0)) - 1, 1)
            step = min(step1, step2)
            median1 = self.median(nums1)
            median2 = self.median(nums2)
            if median1 == median2:
                return median1

            # modify arrays and loop again.
            if median1 < median2:
                nums1 = nums1[step:]
                nums2 = nums2[0:-step]
            else:
                nums1 = nums1[0:-step]
                nums2 = nums2[step:]
