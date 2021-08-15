# -*- coding:utf-8 -*-

# 题目描述
# 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        # 从尾到头➡️先入后出➡️栈
        if listNode is None:
            return []
        stack = []
        head = listNode
        while head.next:
            stack.append(head.val)
            head = head.next
        stack.append(head.val)
        result = []
        while stack:
            result.append(stack.pop())
        return result


if __name__ == "__main__":
    head = ListNode(0)
    p = head
    for i in range(1, 6):
        j = ListNode(i)
        p.next = j
        p = j
        i += 1
    solution = Solution()
    print(solution.printListFromTailToHead(head))
