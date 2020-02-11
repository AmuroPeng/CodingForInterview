# -*- coding:utf-8 -*-

# 题目描述
# 输入一个链表，反转链表后，输出新链表的表头。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        while pHead.next:
            p = pHead.next
            p_next = p.next
            p.next = pHead
            pHead=p
        


if __name__ == "__main__":
    head = ListNode(0)
    p = head
    for i in range(1, 6):
        j = ListNode(i)
        p.next = j
        p = j
        i += 1
    solution = Solution()
    solution.ReverseList(head)
