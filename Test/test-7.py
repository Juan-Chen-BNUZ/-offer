# -*- coding:utf-8 -*-

"""
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""
"""
这个写法是真的你妈牛逼啊
"""

class Solution:
    def Fibonacci(self, n):
        # write code here
        res = [0, 1]
        while len(res) <= n:
            res.append(res[-1] + res[-2])
        return res[n]


#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         if n == 2:
#             return 1
#         if n == 3:
#             return 2
#         if n > 3:
#             return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
# # write code here
