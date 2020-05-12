# -*- coding:utf-8 -*-

"""
题目描述
输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 and not pHead2 :
            return 0
        list1 = []
        list2 = []
        while pHead1:
            list1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            list2.append(pHead2)
            pHead2 = pHead2.next
        length = min(len(list2), len(list1))
        list1.reverse()
        list2.reverse()
        temp = None
        for i in range(length):
            nodeA = list1.pop(0)
            nodeB = list2.pop(0)
            if nodeA == nodeB:
                temp = nodeA
        return temp
