#!/usr/bin/env python3

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        >>> sol = Solution()
        >>> sol.twoSum([2, 7, 11, 15], 9) 
        [0, 1]
        """
        table = dict()
        for index, num in enumerate(nums):
            other = target - num
            if other in table:
                return [table[other], index]
            table[num] = index