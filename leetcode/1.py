#!/usr/bin/env python2.7

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = dict()
        for index, num in enumerate(nums):
            other = target - num
            if other in table:
                return [table[other], index]
            table[num] = index

if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
