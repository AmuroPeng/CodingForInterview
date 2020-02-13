# -*- coding:utf-8 -*-

# 题目描述
# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):  # 递归
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        if pHead1.val > pHead2.val:
            # 需要先把p2.next这些后面排好的链表赋到p1后面，再把p1赋到p2后面
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2
        else:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
