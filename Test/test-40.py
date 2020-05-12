# -*- coding:utf-8 -*-
"""
题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        Num = dict()
        for i in array:
            res = Num.get(i)
            if res is None:
                Num[i] = 1
            else:
                Num[i] += 1
        res = []
        for key in Num.keys():
            if Num[key] == 1:
                res.append(key)
        return res

if __name__ == '__main__':
    A = [2,4,3,6,3,2,5,5]
    print(Solution().FindNumsAppearOnce(A))

