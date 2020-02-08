# -*- coding:utf-8 -*-

# 题目描述
# 输入一个链表，输出该链表中倒数第k个结点


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        # 从尾到头➡️先入后出➡️栈
        if head is None:
            return []
        stack = []
        while head.next:
            stack.append(head.val)
            head = head.next
        stack.append(head.val)
        while k != 1:
            if stack is None:
                return False
            stack.pop()
            k -= 1
        return stack[-1]


if __name__ == "__main__":
    head = ListNode(0)
    p = head
    for i in range(1, 6):
        j = ListNode(i)
        p.next = j
        p = j
        i += 1
    solution = Solution()
    print(solution.FindKthToTail(head, 5))
