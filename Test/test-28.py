# -*- coding:utf-8 -*-
"""
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        Num = dict()
        for i in numbers:
            res = Num.get(i)
            if res is None:
                Num[i] = 1

            else:
                Num[i] += 1

            if Num[i] > len(numbers) / 2:
                return i
        return 0
            # write code here


if __name__ == '__main__':
    A = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(Solution().MoreThanHalfNum_Solution(A))
