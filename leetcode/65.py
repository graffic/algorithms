#!/usr/bin/env python2.7
import re

class Solution(object):
    def __init__(self):
        self.__matcher = re.compile("^[-+]?([0-9]+\.?[0-9]*|[0-9]*\.[0-9]+)([eE][-+]?[0-9]+)?$")

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool

        >>> sol = Solution()
        >>> sol.isNumber("0")
        True
        >>> sol.isNumber(" 0.1 ")
        True
        >>> sol.isNumber("abc")
        False
        >>> sol.isNumber("1 a")
        False
        >>> sol.isNumber("2e10")
        True
        >>> sol.isNumber("3.")
        True
        >>> sol.isNumber(".")
        False
        >>> sol.isNumber(" ")
        False
        >>> sol.isNumber("e9")
        False
        >>> sol.isNumber(".1")
        True
        """
        s = s.strip()
        if len(s) == 0:
            return False
        return self.__matcher.match(s) is not None
