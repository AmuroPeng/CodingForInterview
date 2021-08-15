# -*- coding:utf-8 -*-

# 题目描述
# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 1.用快慢指针检测出有环
        if pHead == None or pHead.next == None or pHead.next.next == None:
            return None
        p_fast = pHead.next
        p_low = pHead
        while p_fast != p_low:
            if p_fast == None or p_low == None:
                return None
            p_fast = p_fast.next.next
            p_low = p_low.next
        # 2.并遍历出环的大小k
        k = 1
        p_fast = p_fast.next
        while p_fast != p_low:
            p_fast = p_fast.next
            k += 1
        # 3.从头开始，一个先走k步一个在起点等待，之后一起遍历。发现两个指针相同➡️入口节点
        p_fast = pHead
        p_low = pHead
        while k!= 0:
            p_fast=p_fast.next
            k-=1
        while p_fast!=p_low:
            p_fast=p_fast.next
            p_low=p_low.next
        return p_fast