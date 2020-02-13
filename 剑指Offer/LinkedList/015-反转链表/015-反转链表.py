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
        if pHead == None:
            return None
        # write code here
        # pFoot = pHead
        # pFoot.val=pHead.val
        # pFoot.next = None
        pFoot = ListNode(pHead.val)
        while pHead.next:
            # p = pHead
            # p.next = pFoot
            # pHead = pHead.next
            # pFoot = p        
            pHead = pHead.next
            p = ListNode(pHead.val)
            p.next = pFoot
            pFoot = p
        # pHead.next = pFoot
        return pFoot


if __name__ == "__main__":
    head = ListNode(0)
    pTemp = ListNode(1)  # 别忘了链表的头节点要一直留着啊！
    head.next=pTemp
    for num in range(2, 6):
        j = ListNode(num)
        pTemp.next = j
        pTemp = j
    # 0 1 2 3 4 5
    solution = Solution()
    solution.ReverseList(head)
    input()
