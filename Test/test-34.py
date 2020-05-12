# -*- coding:utf-8 -*-
"""
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）
"""


class Solution:
    def FirstNotRepeatingChar(self, s):

        # 方法1：
        for i in range(len(s)):
            # print(s.count(s[i]))
            if s.count(s[i]) == 1:
                return i
            else:
                continue
        return -1


# 方法2：
#         Num = dict()
#         for i in s:
#             res = Num.get(i)
#             if res is None:
#                 Num[i] = 1
#
#             else:
#                 Num[i] += 1
#         list_value = list(Num.values())
#         list_key = list(Num.keys())
#         print(list_value)
#         print(list_key)
#
#         j = 0
#         for j in range(len(list_value)):
#             if list_value[j]== 1:
#                 index = list_key[j]
#                 return list_key[j]


if __name__ == '__main__':
    print(Solution().FirstNotRepeatingChar('google'))

# write code here
