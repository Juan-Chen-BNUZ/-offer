# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
题目描述
输入一个链表，输出该链表中倒数第k个结点。
"""


class Solution:
    def FindKthToTail(self, head, k):
        if not head:
            return
        result = []
        while head != None:
            result.append(head)
            head = head.next
        if k > len(result) or k < 1:
            return
        return result[-k]


# write code here
