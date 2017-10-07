#!/usr/bin/env python2.7
import re

class Solution(object):
    def __init__(self):
        self.__matcher = re.compile("^[-+]?([0-9]+\.?[0-9]*|[0-9]*\.[0-9]+)([eE][-+]?[0-9]+)?$")

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if len(s) == 0:
            return False
        return self.__matcher.match(s) is not None

if __name__ == "__main__":
    sol = Solution()
    assert sol.isNumber("0")
    assert sol.isNumber(" 0.1 ")
    assert not sol.isNumber("abc")
    assert not sol.isNumber("1 a")
    assert sol.isNumber("2e10")
    assert sol.isNumber("3.")
    assert not sol.isNumber(".")
    assert not sol.isNumber(" ")
    assert not sol.isNumber("e9")
    assert sol.isNumber(".1")
