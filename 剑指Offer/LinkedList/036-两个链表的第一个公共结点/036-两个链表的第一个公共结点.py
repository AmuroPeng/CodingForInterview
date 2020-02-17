# -*- coding:utf-8 -*-

# 题目描述
# 输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        index_1 = 1
        index_2 = 1
        if pHead1 is None:
            if pHead1 == pHead2:
                return pHead1
            else:
                return None
        else:
            p = pHead1.next
            while p is not None:
                p = p.next
                index_1 += 1
        if pHead2 is None:
            if pHead1 == pHead2:
                return pHead2
            else:
                return None
        else:
            p = pHead2.next
            while p is not None:
                p = p.next
                index_2 += 1
        num = index_1-index_2
        p1 = pHead1
        p2 = pHead2
        if num > 0:
            while num != 0:
                p1 = p1.next
                num -= 1
        else:
            while num != 0:
                p1 = p1.next
                num += 1
        while p1:
            if p1 == p2:
                return p1
            else:
                p1 = p1.next
                p2 = p2.next
