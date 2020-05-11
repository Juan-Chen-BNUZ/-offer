# -*- coding:utf-8 -*-

"""
题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):

        if k > len(tinput):
            return []
        tin = sorted(tinput)
        res = list()
        for i in range(0, k):
            res.append(tin[i])

        return res


if __name__ == '__main__':
    A = [4, 5, 1, 6, 2, 7, 3, 8]
    B = 4
    print(Solution().GetLeastNumbers_Solution(A,B))
# write code here
