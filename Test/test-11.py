# -*- coding:utf-8 -*-
"""
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""


class Solution:
    def NumberOf1(self, n):
        if n == 0:
            return 0
        if n > 0:
            return bin(n).count("1")
        if n < 0:
            return bin(2**32+n).count("1")
            # write code here
