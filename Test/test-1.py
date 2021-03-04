# -*- coding:utf-8 -*-

"""

题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        #         if array == []:
        #             return False
        #         num_row = len(array)
        #         num_col = len(array[0])
        #         for i in range(num_row):
        #             for j in range(num_col):
        #                 if target == array[i][j]:
        #                     return True
        #                 else:
        #                     continue
        # # write code here
        if array == []:
            return False
        row = 0
        col = len(array[0]) - 1
        while row <= len(array) - 1 and col >= 0:
            if target > array[row][col]:
                row = row +1
            elif target < array[row][col]:
                col = col -1
            elif target == array[row][col]:
                return True
        return False

if __name__ == '__main__':
    print(Solution().Find())
