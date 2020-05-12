# -*- coding:utf-8 -*-
"""
题目描述
统计一个数字在排序数组中出现的次数。
"""


class Solution:
    def GetNumberOfK(self, data, k):
        num = 0
        for i in range(len(data)):
            if data[i] == k:
                num += 1
            elif data[i] > k:
                break
        return num
