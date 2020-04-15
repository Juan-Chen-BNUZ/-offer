# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
题目描述
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode == None:
            return []
        else:
            result = []
            while listNode != None:
                result.append(listNode.val)
                listNode = listNode.next
            return result
# write code here
