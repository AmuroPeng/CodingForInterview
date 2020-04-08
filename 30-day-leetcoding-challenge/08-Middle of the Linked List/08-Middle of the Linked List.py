# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p_slow = head
        p_fast = head
        while p_fast.next != None:
            p_slow = p_slow.next
            p_fast = p_fast.next
            if p_fast.next != None:
                p_fast = p_fast.next
                # if p_fast.next == None:
                #     p_slow = p_slow.next
        return p_slow


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    p = head
    p.next = ListNode(2)
    p = p.next
    p.next = ListNode(3)
    p = p.next
    p.next = ListNode(4)
    p = p.next
    p.next = ListNode(5)
    # head.next = ListNode(6)
    print(s.middleNode(head))
