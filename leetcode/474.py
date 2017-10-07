#!/usr/bin/env python2.7
from itertools import permutations


def create_weights(strs):
    cache = {}
    for entry in strs:
        if entry in cache:
            continue
        length = len(entry)
        m = entry.count('0')
        cache[entry] = [m, length -m]
    return cache


def check(cache, strs, m, n):
    how_many = 0
    for entry in strs:
        current_m, current_n = cache[entry]
        m -= current_m
        n -= current_n
        ok = m >=0 and n>=0
        if not ok:
            break
        how_many += 1
    return how_many


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        weights = create_weights(strs)
        for item in strs:
            min_m, min_n = weights[item]
            for min


if __name__ == "__main__":
    sol = Solution()
    strs = ["10","0001","111001","1","0"]
    #assert sol.findMaxForm(strs, 5, 3) == 4
    strs = ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
    assert sol.findMaxForm(strs, 9, 80)
