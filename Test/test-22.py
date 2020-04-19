# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        newroot = [root]
        res = []
        while newroot:
            nextlist = []
            for i in newroot:
                if i.left:
                    nextlist.append(i.left)
                if i.right:
                    nextlist.append(i.right)
                res.append(i.val)
            newroot = nextlist
        return res


# write code here
