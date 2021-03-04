# -*- coding:utf-8 -*-


"""
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""
import functools


class Solution:
    def compare(self, num1, num2):
        t = str(num1) + str(num2)
        s = str(num2) + str(num1)
        if t > s:
            return 1
        elif t < s:
            return -1
        else:
            return 0

    def PrintMinNumber(self, numbers):
        # write code here
        if numbers is None:
            return ""
        lens = len(numbers)
        if lens == 0:
            return ""
        tmpNumbers = sorted(numbers, key = functools.cmp_to_key(self.compare))s
        print(tmpNumbers)
        return int(''.join(str(x) for x in tmpNumbers))

if __name__ == '__main__':
    A = [3,32,321]
    print(Solution().PrintMinNumber(A))