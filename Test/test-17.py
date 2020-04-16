# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):

        def convert(p):
            if p:
                return str(p.val) + convert(p.left) + convert(p.right)
            else:
                return ""

        if convert(pRoot2) in convert(pRoot1) and convert(pRoot2):
            return True
        else:
            return False


        # return convert(pRoot2) in convert(pRoot1) if pRoot2 else False
