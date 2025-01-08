/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    // 1. 迭代
    // if (head === null || head.next === null) return head;
    // let pre, cur, nxt;
    // pre = null;
    // cur = head;
    // nxt = head.next;
    // while (cur !== null) {
    //     cur.next = pre;
    //     pre = cur;
    //     cur = nxt;
    //     if (nxt) nxt = nxt.next;
    // }
    // return pre;

    // 递归
    if (head === null || head.next === null) return head;
    let last = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return last;
};