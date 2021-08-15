# -*- coding:utf-8 -*-

# 题目描述
# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead
        p = ListNode(0)  # 最后删掉
        p.next = pHead
        pHead = p
        root = pHead
        p = root.next
        q = p.next
        if q == None:
            return None if p.val == root.val else root
        flag = -1
        # pHead = root
        while q != None:  # q一直等于p.next
            if q.val == p.val:
                flag = 0
                q = q.next
                p = p.next
            else:
                if flag == 0:  # 状态0是pq相等；1是第一次不等，但是不知q.next和q是否相等;2是可以录入
                    flag = 1
                    q = q.next
                    p = p.next
                elif flag == 1:
                    flag = 2
                else:
                    flag = 2
                    root.next = p
                    root = p
                    q = q.next
                    p = p.next
        if flag != 0:  # 最后一个需要录入
            root.next = p
            root = root.next
        root.next = None
        return pHead.next


if __name__ == "__main__":
    sample = [1, 1]
    sample_head = ListNode(1)
    p = sample_head
    for num in sample:
        q = ListNode(num)
        p.next = q
        p = q
    solution = Solution()
    result = solution.deleteDuplication(sample_head)
    pp = result
    while pp:
        print(pp.val)
        pp = pp.next

        # 错的。审题马虎。其他的没问题
        # if pHead == None:
        #     return None
        # p = pHead
        # if pHead.next == None:
        #     return pHead
        # q = pHead.next
        # while q != None:
        #     if q.val == p.val:
        #         q = q.next
        #     else:
        #         p.next = q
        #         p = q
        #         q = q.next
        # return pHead
