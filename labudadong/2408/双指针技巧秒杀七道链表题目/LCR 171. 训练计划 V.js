/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
  let p1 = headA, p2 = headB;
  let c1 = 0, c2 = 0;
  while (p1) {
      p1 = p1.next;
      c1 += 1;
  }
  while (p2) {
      p2 = p2.next;
      c2 += 1;
  }
  p1 = headA;
  p2 = headB;
  if (c1 > c2) {
      for (let i = 0; i < c1 - c2; i += 1) {
          p1 = p1.next;
      }
  } else {
      for (let i = 0; i < c2 - c1; i += 1) {
          p2 = p2.next;
      }
  }
  while (p1) {
      if (p1 === p2) return p1;
      p1 = p1.next;
      p2 = p2.next;
  }
  return null;
};